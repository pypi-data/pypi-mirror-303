import numpy as np

def plurigaussian_simulation(dim, tree, fields, ldim=100):
    """
    Performs Plurigaussian simulation based on specified dimensions and Gaussian fields, using a decision tree for classification at each point.

    Parameters:
        dim: tuple or list
            The dimensions of the output simulation grid, can be 2D or 3D.
        tree: DecisionTree
            A decision tree object that makes classification decisions based on Gaussian fields.
        fields: list of ndarray
            A list of Gaussian fields, where each field is a numpy array representing a spatial distribution of values. The list should contain 2 fields for 2D simulations and 3 fields for 3D simulations.
        ldim: (int, optional)
            The dimensions of the lithotype in each direction used for decision tree classification. Defaults to 100.

    Returns:
        L: ndarray 
            The lithotype based on the decision tree configuration. An ldim x ldim (or ldim x ldim x ldim for 3D) array where each entry is the decision outcome based on the linearly scaled indices.
        P: ndarray 
            Plurigaussian realisation. An array of the same dimension as `dim` where each entry is the decision outcome based on the values from the `fields` array.

    Notes:
        - The function scales the indices of the lithotype linearly to map the range [-3, 3] across `ldim`.
        - The decision tree is queried with this scaled data to populate the `L` array.
        - For generating the `P` array, the decision tree is queried with actual data points from the `fields`.
    """
    if len(dim) == 2:
        Z1 = fields[0]
        Z2 = fields[1]
        L = np.zeros((ldim,ldim))
        P = np.zeros_like(Z1)
        for ix in range(ldim):
            for iy in range(ldim):
                data = {
                    'Z1' : -3+(ix/ldim)*6,
                    'Z2' : -3+(iy/ldim)*6,
                }
                L[iy, ix] = tree.decide(data)
        for ix in range(dim[0]):
            for iy in range(dim[1]):
                data = {
                    'Z1' : Z1[ix,iy],
                    'Z2' : Z2[ix,iy],
                }
                P[ix,iy] = tree.decide(data)
    elif len(dim) == 3:
        Z1 = fields[0]
        Z2 = fields[1]
        Z3 = fields[2]
        L = np.zeros((ldim,ldim,ldim))
        P = np.zeros_like(Z1)
        for ix in range(ldim):
            for iy in range(ldim):
                for iz in range(ldim):
                    data = {
                        'Z1' : -3+(ix/ldim)*6,
                        'Z2' : -3+(iy/ldim)*6,
                        'Z3' : -3+(iz/ldim)*6,
                    }
                    L[iz, iy, ix] = tree.decide(data)
        for ix in range(dim[0]):
            for iy in range(dim[1]):
                for iz in range(dim[2]):
                    data = {
                        'Z1' : Z1[ix,iy,iz],
                        'Z2' : Z2[ix,iy,iz],
                        'Z3' : Z3[ix,iy,iz],
                    }
                    P[ix,iy,iz] = tree.decide(data)


    return L, P