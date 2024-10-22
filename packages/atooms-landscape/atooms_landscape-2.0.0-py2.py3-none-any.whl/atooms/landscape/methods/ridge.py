import numpy
from scipy.optimize import minimize
from .sd import steepest_descent
from .fire import fire
from .ef import eigenvector_following

class _SameMinimumError(Exception):
    pass

class _ImmediateConvergence(Exception):
    pass

# To use the system dump in sync, we must carry around the coords that were dumped and
# copy in place into them the coordinates of the bisected points.
#
# This is a bit cumbersome. It could be avoided by always copying in place
# the coords upon evaluation directly in the surface. This may incur in some little overhead
# but it is the safest approach.
#
# We could introduce a global update mode in surface to always update coords
#
# It is crucial that we keep the PBC unfolded, but we should check that
# a) the forces are the same
# b) the particles have not moved >L/2

# NOTE: it is very sensitive to convergence criteria. FIRE minimizations must be tight enough gtol = 1e-15 to convergence energies to 10 digits. Otherwise we often experience splitting of basins or 3 distinct basins in bisection.
# NOTE: we are better not folding while displacing along paths

# TODO: in a late PRL 2003 Heuer says he really used steepest descent (but with Buchner he used CG). Is that true? It takes very long in my case. Perhaps I should really add a mixed method that starts SD and switches to CG or FIRE at the bottom where convergence is slow. Monitor W vs steps, until you see it flattens. Check it reproduces the results of bare SD> It did not improve for MB but it will for KA!

# NOTE: if the barrier is very low the final NR steps may slip down to the minima. Perhaps we should have a tighter final bisection for these saddles?

def _bisect(coords_0, coords_1, function, side_step, args=(), iteration=0, inner=False, coords_0_safe=None, coords_1_safe=None):
    # Leave if we are within tolerance
    dist = numpy.mean(numpy.abs(coords_1 - coords_0))
    if dist < side_step:
        print('end bisection, we are converged', dist, '<', side_step)
        #print('coords bi', coords_0.flat[0], coords_1.flat[0])
        if not inner:
            raise _ImmediateConvergence
        return

    #print('bisect:', dist) # coords_0[0], coords_0[1], coords_1[0], coords_1[1] )#function(coords_0, *args), function(coords_1, *args))
    # Find the minima on both sides
    # Note: coords should not be updated by minimize, else we must make copies
    # min_0 = minimize(function, coords_0, method='CG', args=args, jac=gradient, options={'gtol': 1e-10})['x']
    # min_1 = minimize(function, coords_1, method='CG', args=args, jac=gradient, options={'gtol': 1e-10})['x']
    
    # Bisect along a straight line
    coords_c = (coords_0 + coords_1) / 2
    coords_c_copy = coords_c.copy()
    coords_0_copy = coords_0.copy()
    coords_1_copy = coords_1.copy()

    # NOTE: the params must match exactly else we are not on the same surface...
    #print( function(coords_0, *args))
    r_0 = steepest_descent(coords_0, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-10)
    #steepest_descent(coords_0, function, gradient, args=args, maxiter=1000000, dx=1e-4, gtol=1e-3)
    #r_0 = fire(coords_0, function, gradient, gtol=1e-10, args=args)
    u_0 = function('value', coords_0, *args)
    #print( function(coords_1, *args))
    r_1 = steepest_descent(coords_1, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-10)
    #steepest_descent(coords_1, function, gradient, args=args, maxiter=1000000, dx=1e-4, gtol=1e-3)
    #r_1 = fire(coords_1, function, gradient, gtol=1e-10, args=args)
    #fire(coords_1, function, gradient, args=args)
    u_1 = function('value', coords_1, *args)
    #print( function(coords_c, *args))
    r_c = steepest_descent(coords_c, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-10)
    #steepest_descent(coords_c, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-3)
    #r_c = fire(coords_c, function, gradient, gtol=1e-10, args=args)
    #fire(coords_c, function, gradient, args=args)
    u_c = function('value', coords_c, *args)

    print('iter', iteration, 'D_mini', numpy.max(numpy.abs(coords_1 - coords_0)))
    # Restore coordinates to their values before minimization
    coords_c[...] = coords_c_copy
    coords_0[...] = coords_0_copy
    coords_1[...] = coords_1_copy    

    u_s = function('value', coords_c, *args)

    # Compare the energies of the minima: 0-c-1
    ftol = 1e-7
    print('iter', iteration, 'Minima', u_0, u_c, u_1)
    print('iter', iteration, 'Saddle', u_s)    
    print('iter', iteration, 'Barrie', u_s-u_0, u_s-u_1)
    print('iter', iteration, 'sditer', r_0['iterations'], r_1['iterations'], r_c['iterations'])
    if abs(u_c - u_0) < ftol and abs(u_c - u_1) < ftol:
        #print(u_1, u_c, u_0)
        # TODO: in this case, we should revert to previous coords, or have the calling code try again
        if inner:
            coords_0[...] = coords_0_safe
            coords_1[...] = coords_1_safe
            print('Resetting because something went wrong we are in the same minimum: {}'.format(u_c))
        else:
            raise _SameMinimumError('Something wrong we are in the same minimum: {}'.format(u_c))
    elif abs(u_1 - u_0) < ftol:
        print('Warning: Splitting so we stick to 0-c')
        coords_1[...] = coords_c
        #raise ValueError('Something wrong u_0 == u_1: {} {} {}'.format(u_0, u_c, u_1))
    elif abs(u_c - u_0) > ftol and abs(u_c - u_1) > ftol:
        print('Warning: 3 minima so we stick to 0-c : {} {} {}'.format(u_0, u_c, u_1))
        _bisect(coords_0, coords_c, function, side_step, args=args, iteration=iteration, inner=True, coords_0_safe=coords_0_copy, coords_1_safe=coords_1_copy)
        coords_1[...] = coords_c
        #raise ValueError('Something wrong we have 3 distinct minima: {} {} {}'.format(u_0, u_c, u_1))
    elif abs(u_c - u_0) <= ftol:
        # Bisect betweem c and 1
        #print('BISE again c 1')
        _bisect(coords_c, coords_1, function, side_step, args=args, iteration=iteration, inner=True, coords_0_safe=coords_0_copy, coords_1_safe=coords_1_copy)
        coords_0[...] = coords_c
    elif abs(u_c - u_1)  <= ftol:
        # Bisect betweem 0 and c
        #print('BISE again 0 c')
        _bisect(coords_0, coords_c, function, side_step, args=args, iteration=iteration, inner=True, coords_0_safe=coords_0_copy, coords_1_safe=coords_1_copy)
        coords_1[...] = coords_c
        #print('done...')
    else:
        raise ValueError('Something VERY wrong')

    return u_s-u_0, u_s-u_1
    
def _distinct_basins(coords_0, coords_1, function, args=()):
    coords_0_copy = coords_0.copy()
    coords_1_copy = coords_1.copy()

    # TODO: we should be able to optimize gradient / function calculation in SD, it will cut down by a factor 2. But we have no we to access cache_value if we pass function and gradient.
    # Some change in the interface is required
    
    # NOTE: the params must match exactly else we are not on the same surface...
    #print( function(coords_0, *args))
    steepest_descent(coords_0, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-10)
    #steepest_descent(coords_0, function, gradient, args=args, maxiter=1000000, dx=1e-4, gtol=1e-3)
    #fire(coords_0, function, gradient, gtol=1e-12, args=args)
    u_0 = function('value', coords_0, *args)
    #print( function(coords_1, *args))
    steepest_descent(coords_1, function, args=args, maxiter=1000000, dx=1e-4, gtol=1e-10)
    # steepest_descent(coords_1, function, gradient, args=args, maxiter=1000000, dx=1e-4, gtol=1e-3)
    # fire(coords_1, function, gradient, gtol=1e-12, args=args)
    #fire(coords_1, function, gradient, args=args)
    u_1 = function('value', coords_1, *args)
    #print( function(coords_c, *args))

    # Restore coordinates to their values before minimization
    coords_0[...] = coords_0_copy
    coords_1[...] = coords_1_copy    

    # Compare the energies of the minima: 0-c-1
    ftol = 1e-7
    return abs(u_1 - u_0) >= ftol
    

def ridge(coords, function, normal_modes, coords_side=None,
          delta=1e-1, iter_max=100, iter_sd=5, dt=1e-4, side_step=1e-4, callback=None, args=()):
    results = {}
    assert coords_side is not None
    # Roll down along the ridge
    coords_old = coords.copy()
    coords_fire_old = coords.copy()

    sd_dist_old = 0.0
    iteration = 0
    
    U_old, grad = function(('value', 'gradient'), coords, *args)
    W_old = numpy.sum(grad**2) / coords.size
    W = W_old
    down_step = dt
    barriers_old = [0.0, 0.0]  # TODO: set to infty
    delta = None  # TODO: set to infty
    for iteration in range(iter_max):
        
        # Callback
        # if callback is not None:
        #     callback(iteration, coords, coords_side, *args)        
        # Bisect
        # if iteration == 0:
        #     _bisect(coords, coords_side, function, gradient, tol=1e-6, args=args)
        # else:
        #     _bisect(coords, coords_side, function, gradient, args=args)
        try:
            barriers = _bisect(coords, coords_side, function, side_step, args=args, iteration=iteration)
            # We only update this when a full bisection is done (no immediate convergence)
            coords_old[...] = coords.copy()
            coords_fire_old[...] = coords_side.copy()
            delta = [abs(barriers[0] - barriers_old[0]), abs(barriers[1] - barriers_old[1])]
            barriers_old = barriers
        except _ImmediateConvergence:
            pass
        except _SameMinimumError:
            print('Warning: same minimum at iteration:', iteration)
            break

        # Callback
        if callback is not None:
            callback(iteration, coords, coords_side, *args)        
            
        dist = numpy.mean(numpy.abs(coords - coords_side))
        #print('BISE END:', dist)
        if callback is not None:
            callback(iteration, coords, coords_side, *args)        

        U, grad = function(('value', 'gradient'), coords, *args)
        W = numpy.sum(grad**2) / coords.size
        #assert _distinct_basins(coords, coords_side, function, gradient, args=args)
        print('iter', iteration, 'dist', dist, down_step, U, W)
        # TODO: we can stop when the estimated barrier saturates
        # TODO: the step gets small can this slow down convergence

        print('iter', iteration, 'delta', delta[0], delta[1], barriers[0], barriers[1])
        if delta and delta[0] < 1e-4 and delta[1] < 1e-4:
            print('BREAKING because barriers', delta, barriers)
            break
            
        Wtol = 1e-6
        if W < Wtol:
            W = numpy.sum(grad**2) / coords.size
            print('BREAKING!', W, W_old)
            break
        if dt < 1e-10:
            W = numpy.sum(grad**2) / coords.size
            print('BREAKING step too small!', W, W_old)
            break
        if U > U_old:
            print('cut down!', U, U_old)
            dt /= 2
        # else:
        #     dt *= 1.02

            
        W_old = W
        U_old = U        
        # Steepest descent on both sides of the ridge
        # sd_dist = 0.0
        dist = numpy.mean(numpy.abs(coords - coords_side))
        #grad = gradient(coords, *args)
        #grad_side = gradient(coords_side, *args)
        #delta = (grad - grad_side) * dt
        #print('gdelta:', numpy.mean(numpy.abs(delta)))
        steepest_descent(coords, function, args=args, maxiter=iter_sd, dx=dt, gtol=1e-12)
        steepest_descent(coords_side, function, args=args, maxiter=iter_sd, dx=dt, gtol=1e-12)
        #print('after sd', numpy.mean(numpy.abs(coords - coords_side)), dist, dist < numpy.mean(numpy.abs(coords - coords_side)))
        #print('coords sd', coords.flat[0], coords_side.flat[0])

        #fire(coords, function, gradient, args=args, maxiter=iter_sd, dt=down_step)
        #fire(coords_side, function, gradient, args=args, maxiter=iter_sd, dt=down_step)
        down_step_side = numpy.mean(numpy.abs(coords_fire_old - coords_side))
        down_step = numpy.mean(numpy.abs(coords_old - coords))
        ratio = 10.0
        if side_step / down_step > ratio:
            print('cut side_step!')
            side_step /= 2
            
        #print('steps', 'down', down_step, down_step_side, 'side', side_step, 'side/down', side_step / down_step)
        # Reduce number of steps
        #if sd_dist > sd_dist_old:
        #    iter_sd = max(1, iter_sd - 1)
        #sd_dist_old = sd_dist
        
        #steepest_descent(coords, function, gradient, args=args, maxiter=5, dx=1e-4)
        #steepest_descent(coords_side, function, gradient, args=args, maxiter=5, dx=1e-4)
        #min_0 = minimize(function, coords, method='CG', args=args, jac=gradient, options={'gtol': 1e-10})['x']
        #min_1 = minimize(function, coords_side, method='CG', args=args, jac=gradient, options={'gtol': 1e-10})['x']
        # steepest_descent(coords, function, gradient, maxiter=1, dx=1e-6)
        # steepest_descent(coords_side, function, gradient, maxiter=1, dx=1e-6)
        # print('CG:', min_0[0], min_0[1], min_1[0], min_1[1] )
        #print('FIRE:', coords[0], coords[1], coords_side[0], coords_side[1])

    # Fully converge the minimization to the closest transition state with
    # eigenvector following
    # TODO: EF should be combined from outside, not plugged in here
    print('Final bisection')
    try:
        #_bisect(coords, coords_side, function, 1e-6, args=args, iteration=iteration)
        _bisect(coords, coords_side, function, side_step / 10, args=args, iteration=iteration)
    except:
        pass

    print('Start EF after', iteration, W)
    results = eigenvector_following(coords, function, normal_modes, trust_scale_down=1.1, trust_scale_up=1.1, trust_radius=0.001, method='nr', unstable_modes=1, max_iter=20, zero_mode=1e-6, args=args)
    
    if callback is not None:
        callback(iteration, coords, coords_side, *args)        
    results['x'] = coords
    results['bisections'] = iteration
    print()
    return results
    
