import gstools as gs

def create_covariance_model(kernel, dim, variance, length_scale):
    if kernel == 'gau':
        model = gs.Gaussian(dim=len(dim), var=variance, len_scale=length_scale)
    elif kernel == 'mat':
        model = gs.Matern(dim=len(dim), var=variance, len_scale=length_scale)

    return model

def random_field(model, dim, seed=0, mode_no=250):
    if len(dim)==2:
        x = range(dim[0])
        y = range(dim[1])
        srf = gs.SRF(model, seed=seed, mode_no=mode_no)
        field = srf.structured([x, y])
    elif len(dim)==3:
        x = range(dim[0])
        y = range(dim[1])
        z = range(dim[2])
        srf = gs.SRF(model, seed=seed, mode_no=mode_no)
        field = srf.structured([x, y, z])

    return field

