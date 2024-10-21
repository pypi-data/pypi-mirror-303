#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2016-2024                                       ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import dolfin
import glob
import numpy
import os
import time

import myPythonLibrary as mypy

import dolfin_mech as dmech
import dolfin_warp as dwarp

from .NonlinearSolver import NonlinearSolver
from .NonlinearSolver_Relaxation import RelaxationNonlinearSolver

################################################################################

class ReducedKinematicsNewtonNonlinearSolver(RelaxationNonlinearSolver):



    def __init__(self,
            problem,
            motion_model,
            parameters={}):

        self.problem = problem
        self.motion_model = motion_model
        self.printer = self.problem.printer

        # residual & jacobian
        self.res_vec = dolfin.Vector()
        self.jac_mat = dolfin.Matrix()

        # reduced residual & jacobian
        self.JU_vec          = dolfin.Vector()
        self.n_motion_modes  = self.motion_model.n_modes
        self.reduced_disp    = numpy.zeros(self.n_motion_modes)
        self.reduced_res_arr = numpy.zeros(self.n_motion_modes)
        self.reduced_jac_arr = numpy.zeros((self.n_motion_modes, self.n_motion_modes))

        # iterations control
        self.tol_dU      = parameters.get("tol_dU"     , None)
        self.tol_res_rel = parameters.get("tol_res_rel", None)
        self.n_iter_max  = parameters.get("n_iter_max" , 32  )

        # relaxation
        RelaxationNonlinearSolver.__init__(self, parameters=parameters)

        # write iterations
        self.write_iterations = parameters.get("write_iterations", False)

        if (self.write_iterations):
            self.working_folder   = parameters["working_folder"]
            self.working_basename = parameters["working_basename"]

            for filename in glob.glob(self.working_folder+"/"+self.working_basename+"-frame=[0-9]*.*"):
                os.remove(filename)



    def solve(self,
            k_frame=None):

        self.k_frame = k_frame

        if (self.write_iterations):
            self.frame_filebasename = self.working_folder+"/"+self.working_basename+"-frame="+str(self.k_frame).zfill(len(str(self.problem.images_n_frames)))

            self.frame_printer = mypy.DataPrinter(
                names=["k_iter", "res_norm", "res_err_rel", "relax", "dU_norm", "U_norm", "dU_err"],
                filename=self.frame_filebasename+".dat")

            dmech.write_VTU_file(
                filebasename=self.frame_filebasename,
                function=self.problem.U,
                time=0)
        else:
            self.frame_filebasename = None

        self.k_iter = 0
        self.success = False
        self.printer.inc()
        # Test with some initial values
        # self.reduced_disp[-1] += 0.6
        while (True):
            self.k_iter += 1
            self.printer.print_var("k_iter",self.k_iter,-1)

            # linear problem
            self.linear_success = self.linear_solve()
            if not (self.linear_success):
                break

            # relaxation
            self.compute_relax()
            self.reduced_ddisp *= self.relax
            self.problem.dU.vector()[:] *= self.relax
            self.problem.dU_norm *= abs(self.relax)

            # solution update
            self.reduced_disp += 1. * self.reduced_ddisp

            self.problem.U.vector().axpy(1., self.problem.dU.vector())
            self.problem.U_norm = self.problem.U.vector().norm("l2")
            self.printer.print_sci("U_norm",self.problem.U_norm)

            if (self.write_iterations):
                dmech.write_VTU_file(
                    filebasename=self.frame_filebasename,
                    function=self.problem.U,
                    time=self.k_iter)

            # displacement error
            if (self.problem.Uold_norm == 0.):
                if (self.problem.U_norm == 0.):
                    self.problem.dU_err = 0.
                else:
                    self.problem.dU_err = self.problem.dU_norm/self.problem.U_norm
            else:
                self.problem.dU_err = self.problem.dU_norm/self.problem.Uold_norm
            self.printer.print_sci("dU_err",self.problem.dU_err)

            if (self.write_iterations):
                self.frame_printer.write_line([self.k_iter, self.res_norm, self.res_err_rel, self.relax, self.problem.dU_norm, self.problem.U_norm, self.problem.dU_err])

            # exit test
            self.success = True
            if (self.tol_res_rel is not None) and (self.res_err_rel    > self.tol_res_rel):
                self.success = False
            if (self.tol_dU      is not None) and (self.problem.dU_err > self.tol_dU     ):
                self.success = False

            # exit
            if (self.success):
                self.printer.print_str("Nonlinear solver converged…")
                break

            if (self.k_iter == self.n_iter_max):
                self.printer.print_str("Warning! Nonlinear solver failed to converge… (k_frame = "+str(self.k_frame)+")")
                break

        self.printer.dec()

        if (self.write_iterations):
            self.frame_printer.close()
            commandline  = "gnuplot -e \"set terminal pdf noenhanced;"
            commandline += " set output '"+self.frame_filebasename+".pdf';"
            commandline += " set key box textcolor variable;"
            commandline += " set grid;"
            commandline += " set logscale y;"
            commandline += " set yrange [1e-3:1e0];"
            commandline += " plot '"+self.frame_filebasename+".dat' u 1:7 pt 1 lw 3 title 'dU_err', "+str(self.tol_dU)+" lt -1 notitle;"
            commandline += " unset logscale y;"
            commandline += " set yrange [*:*];"
            commandline += " plot '' u 1:4 pt 1 lw 3 title 'relax'\""
            os.system(commandline)

        return self.success, self.k_iter



    def linear_solve(self):

        # Update motion model
        self.motion_model.update_disp(self.reduced_disp, self.problem.U.vector())

        # res_old
        if (self.k_iter > 1):
            if (hasattr(self, "res_old_vec")):
                self.res_old_vec[:] = self.res_vec[:]
            else:
                self.res_old_vec = self.res_vec.copy()
            self.res_old_norm = self.res_norm

        self.problem.call_before_assembly(
            write_iterations=self.write_iterations,
            basename=self.frame_filebasename,
            k_iter=self.k_iter)

        # linear system: residual assembly
        self.printer.print_str("Residual assembly…",newline=False)
        timer = time.time()
        self.problem.assemble_res(
            res_vec=self.res_vec)
        timer = time.time() - timer
        self.printer.print_str(" "+str(timer)+" s",tab=False)

        self.printer.inc()

        # res_norm
        self.res_norm = self.res_vec.norm("l2")
        self.printer.print_sci("res_norm",self.res_norm)

        # dres
        if (self.k_iter > 1):
            if (hasattr(self, "dres_vec")):
                self.dres_vec[:] = self.res_vec[:] - self.res_old_vec[:]
            else:
                self.dres_vec = self.res_vec - self.res_old_vec
            self.dres_norm = self.dres_vec.norm("l2")
            self.printer.print_sci("dres_norm",self.dres_norm)

        # res_err_rel
        if (self.k_iter == 1):
            self.res_err_rel = 1.
        else:
            self.res_err_rel = self.dres_norm / self.res_old_norm
            self.printer.print_sci("res_err_rel",self.res_err_rel)

        # reduced_res_old
        if (self.k_iter > 1):
            if (hasattr(self, "reduced_res_old_arr")):
                self.reduced_res_old_arr[:] = self.reduced_res_arr[:]
            else:
                self.reduced_res_old_arr = self.reduced_res_arr.copy()
            self.reduced_res_old_norm = self.reduced_res_norm

        # linear system: residual reduction
        for i in range(self.n_motion_modes):
            self.reduced_res_arr[i] = self.res_vec.inner(self.motion_model.modes[i].vector())
        # self.printer.print_var("reduced_res_arr",self.reduced_res_arr)

        # reduced_res_norm
        self.reduced_res_norm = numpy.linalg.norm(self.reduced_res_arr)
        # self.printer.print_sci("reduced_res_norm",self.reduced_res_norm)

        # dreduced_res
        if (self.k_iter > 1):
            if (hasattr(self, "reduced_dres_arr")):
                self.reduced_dres_arr[:] = self.reduced_res_arr[:] - self.reduced_res_old_arr[:]
            else:
                self.reduced_dres_arr = self.reduced_res_arr - self.reduced_res_old_arr
            self.reduced_dres_norm = numpy.linalg.norm(self.reduced_dres_arr)
            # self.printer.print_sci("reduced_dres_norm",self.reduced_dres_norm)

        # reduced_res_err_rel
        if (self.k_iter == 1):
            self.reduced_res_err_rel = 1.
        else:
            self.reduced_res_err_rel = self.reduced_dres_norm / self.reduced_res_old_norm
            # self.printer.print_sci("reduced_res_err_rel",self.reduced_res_err_rel)

        self.printer.dec()

        # linear system: matrix assembly
        self.printer.print_str("Jacobian assembly…",newline=False)
        timer = time.time()
        self.problem.assemble_jac(
            jac_mat=self.jac_mat)
        timer = time.time() - timer
        self.printer.print_str(" "+str(timer)+" s",tab=False)

        # linear system: matrix reduction
        for i in range(self.n_motion_modes):
            for j in range(i):
                self.reduced_jac_arr[i,j] = self.reduced_jac_arr[j,i]
            self.jac_mat.mult(self.motion_model.modes[i].vector(), self.JU_vec)
            for j in range(i, self.n_motion_modes):
                self.reduced_jac_arr[i,j] = self.JU_vec.inner(self.motion_model.modes[j].vector())
        # self.printer.print_var("reduced_jac_arr",self.reduced_jac_arr)

        # linear system: solve
        try:
            self.reduced_ddisp = numpy.linalg.solve(self.reduced_jac_arr, -self.reduced_res_arr)
        except:
            self.printer.print_str("Warning! Linear solver failed!",tab=False)
            return False
        # self.printer.print_var("reduced_ddisp",self.reduced_ddisp)

        # Update motion model
        self.motion_model.update_disp(self.reduced_ddisp, self.problem.dU.vector())

        self.printer.inc()

        # dU_norm
        self.problem.dU_norm = self.problem.dU.vector().norm("l2")
        self.printer.print_sci("dU_norm",self.problem.dU_norm)
        if not (numpy.isfinite(self.problem.dU_norm)):
            self.printer.print_str("Warning! Solution increment is NaN! Setting it to 0.",tab=False)
            self.problem.dU.vector().zero()

        self.printer.dec()

        return True
