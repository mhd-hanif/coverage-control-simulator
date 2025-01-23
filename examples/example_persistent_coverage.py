import numpy as np
from coverage_control.agents import load_agent_positions
from coverage_control.animation import animate_voronoi
from coverage_control.coverage_density import CoverageDensity
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial import Voronoi, voronoi_plot_2d

# Initialize the coverage density grid
def update_persistent_density(grid, agent_positions, amplitude=0.8, decay_rate=0.03, recovery_rate=0.01):
    """
    Update the coverage density grid persistently based on agent positions.

    Parameters:
        grid (CoverageDensity): The CoverageDensity object.
        agent_positions (numpy.ndarray): Array of shape (N, 2) representing agent coordinates.
        amplitude (float): Scaling factor for the Gaussian function.
        decay_rate (float): Rate of decay for the Gaussian function.
        recovery_rate (float): Rate of recovery for unvisited points.
    """
    # Increase density for unvisited points
    grid.density += recovery_rate
    grid.density = np.clip(grid.density, 0, 1)

    # Apply Gaussian decay for points near agents
    for agent in agent_positions:
        gaussian = amplitude * np.exp(
            -decay_rate * ((grid.x - agent[0])**2 + (grid.y - agent[1])**2)
        )
        grid.density -= gaussian
        grid.density = np.clip(grid.density, 0, 1)


def visualize_persistent_coverage(positions, output_path, fps=30):
    """
    Create an animation of Voronoi partitions with persistent coverage density.

    Parameters:
        positions (numpy.ndarray): Array of shape (T, N, 2) representing agent positions over time.
        output_path (str): Path to save the generated animation.
        fps (int): Frames per second for the animation.
    """
    x_min, x_max = np.min(positions[:, :, 0]), np.max(positions[:, :, 0])
    y_min, y_max = np.min(positions[:, :, 1]), np.max(positions[:, :, 1])

    # Initialize the coverage density grid
    grid = CoverageDensity(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, resolution=0.05)
    grid.density = np.ones(grid.grid_shape)  # Set initial density to 1

    fig, ax = plt.subplots(figsize=(8, 6))
    interval = 1000 // fps

    def update(frame):
        ax.clear()
        agents = positions[frame]

        # Update density
        update_persistent_density(grid, agents, amplitude=0.8, decay_rate=0.05, recovery_rate=0.03)

        # Compute Voronoi diagram
        vor = Voronoi(agents)

        # Plot density heatmap
        ax.imshow(
            grid.density,
            extent=[grid.x_min, grid.x_max, grid.y_min, grid.y_max],
            origin="lower",
            cmap="jet",
            interpolation="nearest"
        )

        # Plot Voronoi diagram
        voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors="blue", line_width=1)

        # Plot agents
        ax.scatter(agents[:, 0], agents[:, 1], color="red", label="Agents", zorder=5)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_title(f"Timestep: {frame}")
        ax.legend()

    ani = FuncAnimation(fig, update, frames=len(positions), interval=interval, repeat=True)
    ani.save(output_path, writer="imagemagick")
    plt.show()

if __name__ == "__main__":
    # Load agent positions from the CSV file
    csv_file = 'input/agents.csv'  # Path to the CSV file
    timesteps, positions = load_agent_positions(csv_file)

    # Create and save the persistent coverage animation
    visualize_persistent_coverage(positions, 'output/persistent_coverage_example.gif', fps=20)
