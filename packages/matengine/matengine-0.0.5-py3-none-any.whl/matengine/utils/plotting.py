import matplotlib.pyplot as plt
import pyvista as pv
import numpy as np

def plot_array(arr, show=False):
    plt.figure()
    plt.imshow(arr)
    plt.axis('off')
    plt.tight_layout()
    if show: plt.show()

def array_to_vtk(arr, fname='array_out'):
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