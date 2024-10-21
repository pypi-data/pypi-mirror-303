import matplotlib.pyplot as plt
import pyvista as pv
import numpy as np

def plot_array(arr, show=False):
    """
    Plot a 2D array using matplotlib's imshow function.

    Parameters:
        arr: numpy.ndarray 
            The 2D array to be plotted.
        show: bool, optional 
            If True, displays the plot immediately. Default is False.
    """
    plt.figure()
    plt.imshow(arr)
    plt.axis('off')
    plt.tight_layout()
    if show: plt.show()

def array_to_vtk(arr, fname='array_out'):
    """
    Save a 2D or 3D array as a VTK file for visualisation using PyVista.

    Parameters:
        arr: numpy.ndarray 
            The array to be saved as a VTK file. Can be 2D or 3D.
        fname: str, optional 
            The name of the output VTK file (without extension). Default is 'array_out'.

    Notes:
        - For 2D arrays, the function creates a structured grid with zero height (z-dimension).
        - For 3D arrays, the function directly wraps the array as a PyVista grid.
    """
    dim = len(arr.shape)
    if dim == 2:
        # Create a mesh grid
        x = np.arange(arr.shape[1])
        y = np.arange(arr.shape[0])
        x, y = np.meshgrid(x, y)
        # Stack the arrays into 3D space (z is zero)
        points = np.stack((x.flatten(), y.flatten(), np.zeros(x.size)), axis=1)
        # Create the structured grid
        grid = pv.StructuredGrid()
        grid.points = points
        grid.dimensions = [arr.shape[1], arr.shape[0], 1]
        # Assign the values to the grid as scalars
        grid.point_data['values'] = arr.flatten(order='F')  # Use Fortran order for consistency
        # Save the grid to a VTK file
        grid.save(f"{fname}.vtk")
    elif dim == 3:
        # Convert the result to a PyVista grid for saving as .vtk
        grid = pv.wrap(arr)
        grid.save(f"{fname}.vtk")