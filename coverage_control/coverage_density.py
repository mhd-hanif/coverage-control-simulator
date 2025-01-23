import numpy as np
import matplotlib.pyplot as plt

class CoverageDensity:
    """
    Class to handle a 2D mesh grid for coverage density and updates based on agent activity.
    """

    def __init__(self, x_min, x_max, y_min, y_max, resolution=0.01):
        """
        Initialize the 2D mesh grid for coverage density.

        Parameters:
            x_min (float): Minimum x-coordinate of the grid.
            x_max (float): Maximum x-coordinate of the grid.
            y_min (float): Minimum y-coordinate of the grid.
            y_max (float): Maximum y-coordinate of the grid.
            resolution (float): Resolution of the grid (distance between points).
        """
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.resolution = resolution

        # Generate the mesh grid
        self.x, self.y = np.meshgrid(
            np.arange(x_min, x_max, resolution),
            np.arange(y_min, y_max, resolution)
        )
        self.grid_shape = self.x.shape

        # Initialize coverage density to 0 for all grid points
        self.density = np.zeros(self.grid_shape)

    def update_density(self, agent_positions, amplitude=0.8, decay_rate=0.03):
        """
        Update the coverage density based on agent positions using a 2D Gaussian weighting function.

        Parameters:
            agent_positions (numpy.ndarray): Array of shape (N, 2) representing agent coordinates.
            amplitude (float): Scaling factor for the Gaussian function.
            decay_rate (float): Rate of decay for the Gaussian function.
        """
        for agent in agent_positions:
            # Compute the Gaussian influence on the grid for the agent
            gaussian = amplitude * np.exp(
                -decay_rate * ((self.x - agent[0])**2 + (self.y - agent[1])**2)
            )

            # Add the Gaussian influence to the current density
            self.density += gaussian
            self.density = np.clip(self.density, 0, 1)  # Keep density in [0, 1]

    def visualize(self, cmap="jet"):
        """
        Visualize the current coverage density as a heatmap.

        Parameters:
            cmap (str): Matplotlib colormap for visualization.
        """
        plt.figure(figsize=(8, 6))
        plt.imshow(
            self.density,
            extent=[self.x_min, self.x_max, self.y_min, self.y_max],
            origin="lower",
            cmap=cmap,
            interpolation="nearest"
        )
        plt.colorbar(label="Coverage Density")
        plt.title("Coverage Density Heatmap")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
