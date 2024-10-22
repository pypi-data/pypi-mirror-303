from __future__ import print_function
import logging
import numpy


_log = logging.getLogger(__name__)


def steepest_descent(coords, compute, zero=1e-14,
                     maxiter=10000, gtol=1e-10, dx=0.001,
                     dump_coords=False, callback=None, args=()):
    """
    `function` must return the value and the gradient, in this order.
    """
    
    # Initialize data structures
    ndof = coords.size
    result = {}
    result['function_along_path'] = []
    _log.info('# columns:iteration,U,W,n_u\n')

    # Main loop
    Uold = None
    for iteration in range(maxiter):
        U, grad = compute(('value', 'gradient'), coords, *args)
        W = numpy.sum(grad**2) / ndof
        result['function_along_path'].append(U)
        if dump_coords:
            _log.info(('{} {} {} {} {}\n'.format(iteration, U, W, -1, coords)).replace(']', '').replace('[', ''))
        else:
            _log.info('{} {} {} {}\n'.format(iteration, U, W, -1))

        # Callback
        if callback is not None:
            callback(iteration, coords, *args)

        if W < gtol:
            _log.info('# Reached convergence W={} (GTOL)\n'.format(W))
            result['message'] = 'Reached norm gradient tolerance (GTOL)'
            break
        if iteration > 0 and abs(U - Uold) < zero:
            _log.info('# Reached function tolerance (FTOL) !\n')
            result['message'] = 'Reached function tolerance (FTOL)'
            break
        if iteration == maxiter - 1:
            result['message'] = 'Reached maximum number of iterations {} (MAXITER)'.format(maxiter)
            _log.info('# Reached maximum number of iterations {} (MAXITER)\n'.format(maxiter))

        # Update coordinates
        coords -= grad * dx
        
        # Store old values at this step
        Uold = U
        
    result['x'] = coords
    result['function'] = U
    result['iterations'] = iteration
    return result
