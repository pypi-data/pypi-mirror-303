"""
Atooms wrappers to the optimization methods.

They require an atooms compatible `system` object and the desired
`surface` to optimize.
"""

import numpy
from atooms.core.utils import setup_logging
from .helpers import zero_modes, unstable_modes, smallest_nonzero_mode
from .surfaces import potential_energy, force_norm_square


__all__ = ["eigenvector_following", "conjugate_gradient",
           "limited_bfgs", "l_bfgs", "normal_modes_analysis",
           "steepest_descent", "force_minimization", "fire", "ridge"]


def _setup_log(file_log, verbose):
    if file_log is not None:
        setup_logging(level=20, filename=file_log)
    if verbose:
        setup_logging(level=20)


# TODO: add fold parameter to make sure particles are folded during the minimiization
def eigenvector_following(system, surface=potential_energy,
                          trust_radius=0.2, file_log=None,
                          file_debug=None, freeze_iter=-1,
                          freeze_gnorm=-1.0, freeze_modes=None,
                          unstable_modes=-1, max_iter=4000,
                          max_trust=1.0, gtol=1e-10,
                          threshold_error=1.0, trust_scale_up=1.2,
                          kick_tol=-1.0, kick_delta=1e-5,
                          trust_scale_down=1.2, zero_mode=1e-10,
                          callback=None, debug=False, fold=True, verbose=False,
                          W_max=numpy.finfo(float).max):
    from .methods import eigenvector_following as _eigenvector_following

    # Alias (to be deprecated)
    if freeze_modes is not None:
        unstable_modes = int(freeze_modes)
    _setup_log(file_log, verbose)
    #coords = system.dump("position", view=True, order='F')
    coords = system.view("position", order='F')
    stats = _eigenvector_following(coords,
                                   function=surface.compute,
                                   normal_modes=surface.normal_modes,
                                   callback=callback,
                                   args=(system, ),
                                   file_debug=file_debug,
                                   trust_radius=trust_radius,
                                   max_iter=max_iter,
                                   gtol=gtol,
                                   trust_fixed=False,
                                   freeze_iter=freeze_iter,
                                   freeze_gnorm=freeze_gnorm,
                                   unstable_modes=unstable_modes,
                                   max_trust=max_trust,
                                   min_trust=1e-7,
                                   threshold_error=threshold_error,
                                   trust_scale_up=trust_scale_up,
                                   trust_scale_down=trust_scale_down,
                                   kick_tol=kick_tol, kick_delta=kick_delta,
                                   zero_mode=zero_mode,
                                   debug=debug,
                                   W_max=W_max
                                   )
    if fold:
        system.fold()
    return stats


def conjugate_gradient(system, surface=potential_energy, gtol=1e-10, fold=True, verbose=False):
    from scipy.optimize import minimize

    coords = system.dump("position", order='F', flat=True)
    # Clearing the dump is necessary, otherwise the particle data will
    # point to a dead array, it seems, and they will receive no update
    # when dumping with a view.
    # TODO: check gtol in scipy.optimize
    system.dump(clear=True)
    result = minimize(surface.value, coords, method='CG',
                      args=(system, ), jac=surface.gradient,
                      options={'gtol': gtol}
                      )
    result['function'] = surface.value(result['x'], system)
    result['gradient_norm_square'] = numpy.sum(surface.gradient(result['x'], system)**2)
    result.pop('x')
    result.pop('jac')
    if fold:
        system.fold()
    return result


def l_bfgs(system, surface=potential_energy, maxcor=300, gtol=1e-10, fold=True,
           verbose=False):
    from scipy.optimize import minimize

    coords = system.dump("position", order='F', flat=True)
    # Clearing the dump is necessary, otherwise the particle data will
    # point to a dead array, it seems, and they will receive no update
    # when dumping with a view.
    system.dump(clear=True)

    result = minimize(surface.value,
                      coords, method='L-BFGS-B',
                      args=(system, ),
                      jac=surface.gradient,
                      options={'ftol': 1e-14,
                               'gtol': gtol,
                               'iprint': 10 if verbose else -1,
                               'maxcor': maxcor})
    result['iterations'] = result['nit']
    result['function'] = surface.value(result['x'], system)
    result['gradient_norm_square'] = numpy.sum(surface.gradient(result['x'], system)**2)
    result.pop('x')
    result.pop('jac')
    if fold:
        system.fold()
    return result


# Alias
limited_bfgs = l_bfgs


def force_minimization(system, maxcor=300, gtol=1e-10, fold=True, verbose=False):
    result = l_bfgs(system, surface=force_norm_square, maxcor=maxcor,
                    gtol=gtol, fold=fold, verbose=verbose)
    return result


def steepest_descent(system, surface=potential_energy, file_log=None,
                     sample=0, maxiter=4000000, dx=1e-3, gtol=1e-10, fold=True,
                     verbose=False):
    # TODO: drop sample=0
    from .methods import steepest_descent

    _setup_log(file_log, verbose)
    coords = system.dump("position", view=True, order='F')
    result = steepest_descent(coords,
                              surface.compute,
                              maxiter=maxiter,
                              dx=dx,
                              gtol=gtol,
                              args=(system, ),
                              )
    result['gradient_norm_square'] = numpy.sum(surface.gradient(coords, system)**2) / coords.size
    if fold:
        system.fold()
    return result


def fire(system, surface=potential_energy, file_log=None, dt=0.0001,
         dtmax=0.01, gtol=1e-10, maxiter=10000, fold=True, verbose=False):
    from .methods import fire

    _setup_log(file_log, verbose)
    # Flat is needed because of numpy.dot in fire
    # Otherwise flatten v and f in fire
    # system.dump(clear=True)
    #coords = system.dump("position", view=True, flat=True)
    coords = system.dump("position", view=True, order='F')
    result = fire(coords,
                  surface.compute,
                  maxiter=maxiter,
                  gtol=gtol,
                  dt=dt, # starting step
                  dtmax=dtmax,  # maximum step
                  args=(system, )
                  )
    if fold:
        system.fold()
    return result


def ridge(system, system_next, surface=potential_energy,
          file_log=None, gtol=1e-10, maxiter=10000, iter_max=50,
          iter_sd=30, dt=1e-3, side_step=1e-2, fold=True, verbose=False):
    from .methods import ridge

    _setup_log(file_log, verbose)
    surface.update = True
    coords = system.dump("position", view=True, order='F')
    coords_next = system_next.dump('pos', view=True, order='F')
    coords_0 = coords.copy()
    
    #res = fire(system)
    #u_0 = system.potential_energy()
    
    # # Get random direction
    # # displ = numpy.random.random(pos.shape) - 0.5
    # dr = system_next.dump('particle.position_unfolded', order='F', view=True) - \
    #     system.dump('particle.position_unfolded', order='F', view=True)
    # delta = 1e-4
    # while delta < 1:
    #     delta *= 1.2
    #     coords[...] = coords_0 + delta * dr
    #     res = fire(system)
    #     u = system.potential_energy()
    #     #print(delta, abs(u - u_0))
    #     if abs(u - u_0) / abs(u) > 1e-10:
    #         coords = coords_0 + delta * dr  # this must be a copy, else it is a mess
    #         dist = numpy.max(numpy.abs(coords - coords_0))
    #         #print('Starting', delta, dist, u, u_0)
    #         break

    results = ridge(coords_0, surface.compute, surface.normal_modes,
                    coords_side=coords_next, args=(system, ), iter_max=iter_max, iter_sd=iter_sd, dt=dt, side_step=side_step)
    if fold:
        system.fold()
    surface.update = False
    return results


def reaction_path(system, surface=potential_energy, file_log=None,
                  gtol=1e-10, maxiter=10000, verbose=False):
    #from .methods import fire

    _setup_log(file_log, verbose)
    results = {}
    coords = system.dump("position", view=True, order='F')
    coords_0 = coords.copy()
    res = normal_modes_analysis(system, surface=surface)
    assert res['number_of_unstable_modes'] == 1
    dr = res['eigenvector'][0]
    delta = 1e-4
    coords += dr * delta
    res = fire(system)
    #res = steepest_descent(system)
    #print(res)
    #system.fold()
    results['u_0'] = res['function']
    results['function_along_path'] = res['function_along_path'][::-1]
    #results['x_0'] = coords.copy()

    coords[...] = coords_0
    coords -= dr * delta
    res = fire(system)
    #res = steepest_descent(system)
    #print(res)
    #system.fold()
    results['u_1'] = res['function']
    results['function_along_path'] += res['function_along_path']
    #results['x_1'] = coords.copy()
    
    return results


def normal_modes_analysis(system, surface=potential_energy):
    from .helpers import participation_ratio

    coords = system.dump("position", view=True, order='F')
    eigvalues, eigvectors = potential_energy.normal_modes(coords, system)
    system.eigvalues = eigvalues
    system.eigvectors = eigvectors

    N = len(system.particle)
    L = system.cell.side[0]

    db = {}
    db['eigenvalue'] = eigvalues
    db['eigenvector'] = eigvectors
    db['number_of_zero_modes'] = zero_modes(eigvalues)
    db['number_of_unstable_modes'] = unstable_modes(eigvalues)
    db['smallest_nonzero_mode'] = smallest_nonzero_mode(eigvalues)
    db['fraction_of_unstable_modes'] = float(unstable_modes(eigvalues)) / len(eigvalues)
    db['potential_energy'] = system.potential_energy(per_particle=True, cache=True)
    db['force_norm_square'] = system.force_norm_square(per_particle=True, cache=True)
    db['participation_ratio'] = [participation_ratio(eigvectors[i]) for i in range(len(eigvectors))]
    db['participation_ratio_over_L'] = [_ / L for _ in db['participation_ratio']]
    db['participation_ratio_over_N'] = [_ / N for _ in db['participation_ratio']]

    return db


# def compose(system, method, gtol, kwargs=None, surface=potential_energy,
#             file_log=None, verbose=False):

#     _setup_log(file_log, verbose)
#     if kwargs is None:
#         kwargs = [{}] * len(method)
#     for _method, _kwargs, _gtol in zip(method, kwargs, gtol):
#         result = _method(system,
#                          surface=surface,
#                          gtol=_gtol,
#                          **_kwargs
#         )
#         # TODO: do not fold until the last step
#         # TODO: merge all standard fields of results: iterations, function_along_path, gradient_norm_square_along_path
#     return result
