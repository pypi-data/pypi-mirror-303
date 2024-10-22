import numpy
import logging
_log = logging.getLogger(__name__)


def fire(coords, compute,
         finc=1.1,  # increment time step if dot(f,v) is positive
         fdec=0.5,  # decrement time step if dot(f,v) is negative
         acoef0=0.1,  # coefficient of skier force update
         falpha=0.99,  # decrease of skier force component acoef if projection dot(f,v) is positive
         dt=0.0001,  # starting step
         dtmax=0.01,  # maximum step
         gtol=1e-10,
         maxiter=100000,
         callback=None,
         args=()):

    # Initialization
    # TODO: what about masses for mixtures? -> preconditioning
    mass = 4.0  # mass of atoms (it is useless at this stage, it amounts to redefine the dt)
    result = {}
    acoef = acoef0
    v = numpy.zeros_like(coords)
    result['function_along_path'] = []
    for iteration in range(maxiter):
        # Evaluate force
        value, grad = compute(('value', 'gradient'), coords, *args)
        f = - grad
        result['function_along_path'].append(value)
        # Callback
        if callback is not None:
            callback(iteration, coords, *args)
        # Convergence
        W = numpy.sum(f**2) / f.size
        if W < gtol:
            result['success'] = True
            result['message'] = 'Reached norm gradient tolerance (GTOL)'
            _log.info('# Reached convergence W={} after n_iter={} (GTOL)\n'.format(W, iteration))
            break
        # Evaluate projection of force to velocity
        # TODO: optimize
        _v, _f = v.flatten(), f.flatten()
        vf = numpy.dot(_v, _f)
        vv = numpy.dot(_v, _v)
        ff = numpy.dot(_f, _f)
        if vf < 0:
            v = 0
            dt = dt * fdec
            acoef = acoef0
        elif vf > 0:
            cF = acoef * (vv / ff)**0.5
            cV = 1 - acoef
            v = cV * v + cF * f
            dt = min(dt * finc, dtmax)
            acoef = acoef * falpha
        # MD step using leap-frog
        v = v + dt / mass * f
        coords[...] = coords + dt * v
        # TODO: do we need pbcs?
        #print(coords[:, :5])

    result['iterations'] = iteration
    result['function'] = compute('value', coords, *args)
    result['gradient_norm_square'] = W
    return result
