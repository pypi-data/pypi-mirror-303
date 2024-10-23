import gstools as gs

def create_covariance_model(kernel, dim, variance, length_scale):
    """
    Create a covariance model based on the specified kernel type.

    Parameters:
        kernel : str
            The type of kernel to use for the covariance model. Options are:
                - 'gau': Gaussian kernel
                - 'mat': Matern kernel
        dim : list or tuple
            The dimensions for the covariance model.
        variance : float
            The variance parameter for the covariance model.
        length_scale : float
            The length scale parameter for the covariance model.

    Returns:
        model : gstools.Gaussian or gstools.Matern
            The created covariance model using the specified kernel, dimension,
            variance, and length scale parameters.
    """
    if kernel == 'gau':
        model = gs.Gaussian(dim=len(dim), var=variance, len_scale=length_scale)
    elif kernel == 'mat':
        model = gs.Matern(dim=len(dim), var=variance, len_scale=length_scale)

    return model

def random_field(model, dim, seed=0, mode_no=250):
    """
    Generates a random field using a stochastic random field (SRF) model from gstools.

    Parameters:
        model: 
            A geostatistical model from gstools to be used for generating the random field. Typically, this is an instance of a Gaussian process model.
        dim: tuple or list 
            A tuple or list representing the dimensions of the random field. It should contain either two or three elements for 2D or 3D fields respectively.
        seed: int, optional 
            A seed value for the random number generator to ensure reproducibility. Default is 0.
        mode_no: int, optional 
            The number of modes to use for the stochastic simulation. Default is 250.

    Returns:
        numpy.ndarray: 
            The generated random field, either 2D or 3D depending on the input dimensions.
    """
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

