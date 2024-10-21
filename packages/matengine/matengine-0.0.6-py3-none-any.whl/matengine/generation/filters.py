import numpy as np
from skimage.morphology import convex_hull_image
from scipy.ndimage import label

def convex_hull(pluri, thresh=5):
    """
    Apply a convex hull transformation to each connected component in an image that exceeds a specified size threshold.

    Parameters:
        pluri: ndarray
            A multi-dimensional numpy array representing an image. The function supports both 2D and 3D images.
        thresh: int, optional 
            The threshold value for the minimum number of voxels/pixels a connected component must have to be considered for the convex hull transformation. Defaults to 5.

    Returns:
        ndarray: 
            A new image array of the same dimensions as `pluri` where each significant connected component (as determined by `thresh`) has been transformed using the convex hull operation.

    Notes:
        - For 2D images, the function calculates the convex hull for each connected component directly.
        - For 3D images, the convex hull is applied slice by slice and then accumulated, assuming that `pluri` represents a stack of 2D slices.
        - The function uses scipy's `label` function to identify connected components and skimage's `convex_hull_image` for the convex hull transformation.
    """
    dim = len(pluri.shape)
    if dim == 2:
        # Applies a convex hull to each connected component in 3D
        x, y, = pluri.shape
        labeled_array, num_features = label(pluri)
        cvxhull = np.zeros((x, y))

        for il in range(1, num_features + 1):
            tmp = np.zeros((x, y))
            
            # Count the number of voxels in the current labeled component
            count = np.sum(labeled_array == il)
            
            # If the component is larger than the threshold, apply convex hull
            if count > thresh:
                tmp[labeled_array == il] = 1
                tmp = convex_hull_image(tmp)
                tmp = tmp.astype(int)
                tmp[tmp != 0] = np.max(pluri[labeled_array == il])
                

            cvxhull += tmp
    elif dim == 3:
        # Applies a convex hull to each connected component in 3D
        x, y, z = pluri.shape
        labeled_array, num_features = label(pluri)
        cvxhull = np.zeros((x, y, z))

        
        for il in range(1, num_features + 1):
            tmp = np.zeros((x, y, z))
            count = 0
            
            # Count the number of voxels in the current labeled component
            for iz in range(z):
                for iy in range(y):
                    for ix in range(x):
                        if labeled_array[iz, iy, ix] == il:
                            count += 1
            
            # If the component is larger than the threshold, apply convex hull
            if count > thresh:
                for iz in range(z):
                    for iy in range(y):
                        for ix in range(x):
                            if labeled_array[iz, iy, ix] == il:
                                tmp[iz, iy, ix] = 1
                tmp = convex_hull_image(tmp)

            cvxhull += tmp

        # # Only for 2 phase
        # for iz in range(z):
        #     for iy in range(y):
        #         for ix in range(x):
        #             if cvxhull[iz, iy, ix] != 0:
        #                 cvxhull[iz, iy, ix] = 1

    return cvxhull