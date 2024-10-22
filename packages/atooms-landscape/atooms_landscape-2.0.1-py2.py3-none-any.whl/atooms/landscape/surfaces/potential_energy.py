from f2py_jit import jit

cache_value = False
update = False

# All views for update are set with an explicit order='F' argument (atooms 3.20)

def normal_modes(coords, system):
    import os
    from scipy.linalg import eigh as eig

    if update:
        pos = system.dump('pos', view=True, order='F')
        pos[...] = coords  # or copy()?
    
    # Compute Hessian
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    system.compute_interaction('hessian')
    ndof = len(system.particle) * system.number_of_dimensions

    # Kernel to scale hessian by masses
    _f90 = jit("""
subroutine scale(H, m)
double precision, intent(inout) :: H(:,:,:,:)
double precision, intent(in) :: m(:)
integer :: i, j
do i = 1, size(H, 2)
  do j = 1, size(H, 4)
    H(:,i,:,j) = H(:,i,:,j) / (m(i)*m(j))**0.5
  end do
end do
end subroutine
""")
    mass = system.dump('particle.mass')
    _f90.scale(system.interaction.hessian, mass)    
    
    # Diagonalize the scaled hessian matrix
    hessian = system.interaction.hessian.reshape((ndof, ndof), order='F')
    eigvalues, eigvectors = eig(hessian)
    eigvalues = [float(_) for _ in eigvalues]

    # Set eigenvectors in original (ndim, N) shape
    tmp_eigv = []
    for i in range(len(eigvalues)):
        tmp_eigv.append(eigvectors[:, i].reshape((system.number_of_dimensions, len(system.particle)), order='F'))
    eigvectors = tmp_eigv
    return eigvalues, eigvectors


def _pack_coords(coords, system):
    ndim = system.number_of_dimensions
    for i, p in enumerate(system.particle):
        p.position[:] = coords[ndim * i: ndim * (i + 1)]


def value(coords, system):
    """
    if `cache` is `True` we do not recompute the value but assume it
    has already been computed because e.g. of a call to `gradient`
    """
    if cache_value:
        return system.potential_energy(cache=True, per_particle=False)
    else:
        if len(coords.shape) == 1:
            _pack_coords(coords, system)
        elif update:
            pos = system.dump('pos', view=True, order='F')
            pos[...] = coords  # or copy()?
        return system.potential_energy(per_particle=False)


def gradient(coords, system):
    if len(coords.shape) == 1:
        _pack_coords(coords, system)
        system.compute_interaction("forces")
        return - system.interaction.forces.flatten(order='F')
    else:
        if update:
            pos = system.dump('pos', view=True, order='F')
            pos[...] = coords  # or copy()?
        system.compute_interaction("forces")
        return - system.interaction.forces


def compute(what, coords, system):
    if len(coords.shape) == 1:
        _pack_coords(coords, system)
        system.compute_interaction("forces")
        grad = - system.interaction.forces.flatten(order='F')
    else:
        if update:
            pos = system.dump('pos', view=True, order='F')
            pos[...] = coords  # or copy()?
        system.compute_interaction("forces")
        grad = - system.interaction.forces

    val = system.potential_energy(per_particle=False)
    if what == 'value':
        return val
    elif what == 'gradient':
        return grad
    elif what == ('value', 'gradient'):
        return val, grad
