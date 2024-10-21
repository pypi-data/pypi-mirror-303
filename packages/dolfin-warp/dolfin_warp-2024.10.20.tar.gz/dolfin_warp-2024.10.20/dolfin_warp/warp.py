#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2016-2024                                       ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import dolfin

import dolfin_warp as dwarp

################################################################################

def warp(
        working_folder                              : str,
        working_basename                            : str,
        images_folder                               : str,
        images_basename                             : str,
        images_grad_basename                        : str         = None                            ,
        images_ext                                  : str         = "vti"                           , # vti, vtk
        images_n_frames                             : int         = None                            ,
        images_ref_frame                            : int         = 0                               ,
        images_quadrature                           : int         = None                            ,
        images_quadrature_from                      : str         = "points_count"                  , # points_count, integral
        images_expressions_type                     : str         = "cpp"                           , # cpp
        images_static_scaling                       : bool        = False                           ,
        images_dynamic_scaling                      : bool        = False                           ,
        images_char_func                            : bool        = True                            ,
        images_is_cone                              : bool        = False                           ,
        mesh                                        : dolfin.Mesh = None                            ,
        mesh_folder                                 : str         = None                            ,
        mesh_basename                               : str         = None                            ,
        mesh_degree                                 : int         = 1                               ,
        regul_type                                  : str         = "continuous-equilibrated"       , # continuous-linear-equilibrated, continuous-linear-elastic, continuous-equilibrated, continuous-elastic, continuous-hyperelastic, discrete-simple-equilibrated, discrete-simple-elastic, discrete-linear-equilibrated, discrete-linear-tractions, discrete-linear-tractions-normal, discrete-linear-tractions-tangential, discrete-linear-tractions-normal-tangential, discrete-equilibrated, discrete-tractions, discrete-tractions-normal, discrete-tractions-tangential, discrete-tractions-normal-tangential
        regul_types                                 : list        = None                            ,
        regul_model                                 : str         = "ogdenciarletgeymonatneohookean", # hooke, kirchhoff, ogdenciarletgeymonatneohookean, ogdenciarletgeymonatneohookeanmooneyrivlin
        regul_models                                : list        = None                            ,
        regul_quadrature                            : int         = None                            ,
        regul_level                                 : float       = 0.                              ,
        regul_levels                                : list        = None                            ,
        regul_poisson                               : float       = 0.                              ,
        regul_b                                     : float       = None                            ,
        regul_volume_subdomain_data                               = None                            ,
        regul_volume_subdomain_id                                 = None                            ,
        regul_surface_subdomain_data                              = None                            ,
        regul_surface_subdomain_id                                = None                            ,
        tangent_type                                : str         = "Idef"                          , # Idef
        residual_type                               : str         = "Iref"                          , # Iref
        relax_type                                  : str         = None                            , # constant, aitken, backtracking, gss
        relax_init                                  : float       = 1.                              , # 1.
        relax_backtracking_factor                   : float       = None                            ,
        relax_tol                                   : float       = None                            ,
        relax_n_iter_max                            : int         = None                            ,
        relax_must_advance                          : bool        = None                            ,
        normalize_energies                          : bool        = False                           ,
        initialize_U_from_file                      : bool        = False                           ,
        initialize_U_folder                         : str         = None                            ,
        initialize_U_basename                       : str         = None                            ,
        initialize_U_ext                            : str         = "vtu"                           ,
        initialize_U_array_name                     : str         = "displacement"                  ,
        initialize_U_method                         : str         = "dofs_transfer"                 , # dofs_transfer, interpolation, projection
        initialize_DU_with_DUold                    : bool        = False                           ,
        register_ref_frame                          : bool        = False                           ,
        iteration_mode                              : str         = "normal"                        , # normal, loop
        gimic                                       : bool        = False                           ,
        gimic_texture                               : str         = "no"                            ,
        gimic_resample                              : int         = 1                               ,
        nonlinearsolver                             : str         = "newton"                        , # newton, CMA
        tol_res                                     : float       = None                            , # None
        tol_res_rel                                 : float       = None                            ,
        tol_dU                                      : float       = None                            ,
        tol_dU_rel                                  : float       = None                            ,
        tol_im                                      : float       = None                            , # None
        n_iter_max                                  : int         = 100                             ,
        continue_after_fail                         : bool        = False                           ,
        write_qois_limited_precision                : bool        = False                           ,
        write_VTU_files                             : bool        = True                            ,
        write_VTU_files_with_preserved_connectivity : bool        = False                           ,
        write_XML_files                             : bool        = False                           ,
        print_refined_mesh                          : bool        = False                           , # False
        print_iterations                            : bool        = False                           ,
        silent                                      : bool        = False                           ):

    assert (images_expressions_type == "cpp"),\
        "Python image expression are deprecated. Aborting."
    assert (tangent_type == "Idef"),\
        "tangent_type must be \"Idef\". Aborting."
    assert (residual_type == "Iref"),\
        "residual_type must be \"Iref\". Aborting."
    assert (relax_init == 1.),\
        "relax_init must be 1. Aborting."
    assert (not ((initialize_U_from_file) and (initialize_DU_with_DUold))),\
        "Cannot initialize U from file and DU with DUold together. Aborting."
    assert (tol_res is None),\
        "tol_res is deprecated. Aborting."
    assert (tol_im is None),\
        "tol_im is deprecated. Aborting."
    assert (print_refined_mesh == 0),\
        "print_refined_mesh is deprecated. Aborting."

    # assert (regul_type is not None) or (regul_types is not None),\
    #     "Must provide \"regul_type\" or \"regul_types\". Aborting."
    # assert (regul_model is not None) or (regul_models is not None),\
    #     "Must provide \"regul_model\" or \"regul_models\". Aborting."
    # assert (regul_level is not None) or (regul_levels is not None),\
    #     "Must provide \"regul_level\" or \"regul_levels\". Aborting."

    # assert (regul_type is None) or (regul_types is None),\
    #     "Cannot provide both \"regul_type\" and \"regul_types\". Aborting."
    # assert (regul_model is None) or (regul_models is None),\
    #     "Cannot provide both \"regul_model\" and \"regul_models\". Aborting."
    # assert (regul_level is None) or (regul_levels is None),\
    #     "Cannot provide both \"regul_level\" and \"regul_levels\". Aborting."

    if (regul_types is not None):
        if (regul_models is not None):
            assert (len(regul_models) == len(regul_types))
        else:
            regul_models = [regul_model]*len(regul_types)
        if (regul_levels is not None):
            assert (len(regul_levels) == len(regul_types))
        else:
            regul_levels = [regul_level]*len(regul_types)
    else:
        assert (regul_type is not None)
        if ("tractions" in regul_type):
            if (regul_type.startswith("discrete-linear-equilibrated-")):
                regul_types = ["discrete-linear-equilibrated"]
                if (regul_type == "discrete-linear-equilibrated-tractions"):
                    regul_types += ["discrete-linear-tractions"]
                elif (regul_type == "discrete-linear-equilibrated-tractions-normal"):
                    regul_types += ["discrete-linear-tractions-normal"]
                elif (regul_type == "discrete-linear-equilibrated-tractions-tangential"):
                    regul_types += ["discrete-linear-tractions-tangential"]
                elif (regul_type == "discrete-linear-equilibrated-tractions-normal-tangential"):
                    regul_types += ["discrete-linear-tractions-normal-tangential"]
            elif (regul_type.startswith("discrete-equilibrated-")):
                regul_types = ["discrete-equilibrated"]
                if (regul_type == "discrete-equilibrated-tractions"):
                    regul_types += ["discrete-tractions"]
                elif (regul_type == "discrete-equilibrated-tractions-normal"):
                    regul_types += ["discrete-tractions-normal"]
                elif (regul_type == "discrete-equilibrated-tractions-tangential"):
                    regul_types += ["discrete-tractions-tangential"]
                elif (regul_type == "discrete-equilibrated-tractions-normal-tangential"):
                    regul_types += ["discrete-tractions-normal-tangential"]
            else: assert (0), "Unknown regul_type ("+str(regul_type)+"). Aborting."
            regul_models = [regul_model  ]*2
            regul_levels = [regul_level/2]*2
        else:
            regul_types  = [regul_type ]
            regul_models = [regul_model]
            regul_levels = [regul_level]
    # print (regul_types)
    # print (regul_models)
    # print (regul_levels)

    problem = dwarp.WarpingProblem(
        mesh=mesh,
        mesh_folder=mesh_folder,
        mesh_basename=mesh_basename,
        U_degree=mesh_degree,
        silent=silent)

    images_series = dwarp.ImagesSeries(
        folder=images_folder,
        basename=images_basename,
        grad_basename=images_grad_basename,
        n_frames=images_n_frames,
        ext=images_ext,
        printer=problem.printer)

    if (images_quadrature is None):
        problem.printer.print_str("Computing quadrature degree…")
        problem.printer.inc()
        if (images_quadrature_from == "points_count"):
            images_quadrature = dwarp.compute_quadrature_degree_from_points_count(
                image_filename=images_series.get_image_filename(k_frame=images_ref_frame),
                mesh=problem.mesh,
                verbose=1)
        elif (images_quadrature_from == "integral"):
            images_quadrature = dwarp.compute_quadrature_degree_from_integral(
                image_filename=images_series.get_image_filename(k_frame=images_ref_frame),
                mesh=problem.mesh,
                verbose=1)
        else:
            assert (0), "\"images_quadrature_from\" (="+str(images_quadrature_from)+") must be \"points_count\" or \"integral\". Aborting."
        problem.printer.print_var("images_quadrature",images_quadrature)
        problem.printer.dec()

    image_w = 1.-sum(regul_levels)
    assert (image_w > 0.),\
        "1.-sum(regul_levels) must be positive. Aborting."

    if (gimic):
        generated_image_energy = dwarp.GeneratedImageContinuousEnergy(
            problem=problem,
            images_series=images_series,
            quadrature_degree=images_quadrature,
            texture=gimic_texture,
            w=image_w,
            ref_frame=images_ref_frame,
            resample=gimic_resample)
        problem.add_image_energy(generated_image_energy)
    else:
        warped_image_energy = dwarp.WarpedImageContinuousEnergy(
            problem=problem,
            images_series=images_series,
            quadrature_degree=images_quadrature,
            w=image_w,
            ref_frame=images_ref_frame,
            w_char_func=images_char_func,
            im_is_cone=images_is_cone,
            static_scaling=images_static_scaling,
            dynamic_scaling=images_dynamic_scaling)
        problem.add_image_energy(warped_image_energy)

    for regul_type, regul_model, regul_level in zip(regul_types, regul_models, regul_levels):
        if (regul_level>0):
            name_suffix  = ""
            name_suffix += ("_"+    regul_type  )*(len(regul_types )>1)
            name_suffix += ("_"+    regul_model )*(len(regul_models)>1)
            name_suffix += ("_"+str(regul_level))*(len(regul_levels)>1)
            regul_b_ = None
            if regul_type.startswith("continuous"):
                regularization_energy_type = dwarp.RegularizationContinuousEnergy
                if regul_type.startswith("continuous-linear"):
                    regul_type_ = regul_type.split("-",2)[2]
                else:
                    regul_type_ = regul_type.split("-",1)[1]
            elif regul_type.startswith("discrete-simple"):
                regularization_energy_type = dwarp.SimpleRegularizationDiscreteEnergy
                regul_type_ = regul_type.split("-",2)[2]
            elif regul_type.startswith("discrete"):
                if ("equilibrated" in regul_type):
                    regularization_energy_type = dwarp.VolumeRegularizationDiscreteEnergy
                    regul_b_ = regul_b
                elif ("tractions" in regul_type):
                    regularization_energy_type = dwarp.SurfaceRegularizationDiscreteEnergy
                else: assert (0), "regul_type (= "+str(regul_type)+") unknown. Aborting."
                if regul_type.startswith("discrete-linear"):
                    regul_type_ = regul_type.split("-",2)[2]
                else:
                    regul_type_ = regul_type.split("-",1)[1]
            else: assert (0), "regul_type (= "+str(regul_type)+") unknown. Aborting."
            regularization_energy = regularization_energy_type(
                name="reg"+name_suffix,
                problem=problem,
                w=regul_level,
                type=regul_type_,
                model=regul_model,
                poisson=regul_poisson,
                b_fin=regul_b_,
                volume_subdomain_data=regul_volume_subdomain_data,
                volume_subdomain_id=regul_volume_subdomain_id,
                surface_subdomain_data=regul_surface_subdomain_data,
                surface_subdomain_id=regul_surface_subdomain_id,
                quadrature_degree=regul_quadrature)
            problem.add_regul_energy(regularization_energy)

    if (normalize_energies):
        dwarp.compute_energies_normalization(
            problem=problem,
            verbose=1)

    if (nonlinearsolver == "newton"):
        solver = dwarp.NewtonNonlinearSolver(
            problem=problem,
            parameters={
                "working_folder":working_folder,
                "working_basename":working_basename,
                "relax_type":relax_type,
                "relax_backtracking_factor":relax_backtracking_factor,
                "relax_tol":relax_tol,
                "relax_n_iter_max":relax_n_iter_max,
                "relax_must_advance":relax_must_advance,
                "tol_res_rel":tol_res_rel,
                "tol_dU":tol_dU,
                "tol_dU_rel":tol_dU_rel,
                "n_iter_max":n_iter_max,
                "write_iterations":print_iterations})
    elif (nonlinearsolver == "reduced_kinematic_newton"):
        motion = dwarp.MotionModel(
            problem=problem,
            type="translation_and_scaling")
        solver = dwarp.ReducedKinematicsNewtonNonlinearSolver(
            problem=problem,
            motion_model=motion,
            parameters={
                "working_folder":working_folder,
                "working_basename":working_basename,
                "relax_type":relax_type,
                "relax_backtracking_factor":relax_backtracking_factor,
                "relax_tol":relax_tol,
                "relax_n_iter_max":relax_n_iter_max,
                "relax_must_advance":relax_must_advance,
                "tol_res_rel":tol_res_rel,
                "tol_dU":tol_dU,
                "tol_dU_rel":tol_dU_rel,
                "n_iter_max":n_iter_max,
                "write_iterations":print_iterations})
    elif (nonlinearsolver == "cma"):
        solver = dwarp.CMANonlinearSolver(
            problem=problem,
            parameters={
                "working_folder":working_folder,
                "working_basename":working_basename,
                "write_iterations":print_iterations})

    image_iterator = dwarp.ImageIterator(
        problem=problem,
        solver=solver,
        parameters={
            "working_folder":working_folder,
            "working_basename":working_basename,
            "register_ref_frame":register_ref_frame,
            "initialize_U_from_file":initialize_U_from_file,
            "initialize_U_folder":initialize_U_folder,
            "initialize_U_basename":initialize_U_basename,
            "initialize_U_ext":initialize_U_ext,
            "initialize_U_array_name":initialize_U_array_name,
            "initialize_U_method":initialize_U_method,
            "initialize_DU_with_DUold":initialize_DU_with_DUold,
            "write_qois_limited_precision":write_qois_limited_precision,
            "write_VTU_files":write_VTU_files,
            "write_VTU_files_with_preserved_connectivity":write_VTU_files_with_preserved_connectivity,
            "write_XML_files":write_XML_files,
            "iteration_mode":iteration_mode,
            "continue_after_fail":continue_after_fail})

    success = image_iterator.iterate()

    problem.close()

    return success

fedic2 = warp

########################################################################

if (__name__ == "__main__"):
    import fire
    fire.Fire(warp)
