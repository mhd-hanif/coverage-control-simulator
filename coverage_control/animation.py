import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

def animate_voronoi(positions, output_path, fps=30):
    """
    Create an animation of Voronoi partitions with automatic axis adjustment and correct aspect ratio.
    
    Parameters:
        positions (numpy.ndarray): Array of shape (T, N, 2) representing agent positions over time.
        output_path (str): Path to save the generated animation.
        fps (int): Frames per second for the animation.
    """
    # Determine data bounds for x and y
    x_min, x_max = np.min(positions[:, :, 0]), np.max(positions[:, :, 0])
    y_min, y_max = np.min(positions[:, :, 1]), np.max(positions[:, :, 1])

    # Calculate the figure aspect ratio based on data ranges
    aspect_ratio = (x_max - x_min) / (y_max - y_min)
    fig_width = 8  # Base width
    fig_height = fig_width / aspect_ratio  # Adjust height to match aspect ratio

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    interval = 1000 // fps  # Convert FPS to milliseconds per frame

    def update(frame):
        ax.clear()
        agents = positions[frame]
        vor = Voronoi(agents)
        voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=1, point_size=10)
        ax.scatter(agents[:, 0], agents[:, 1], color='red', label='Agents', zorder=5)
        ax.set_xlim(x_min, x_max)  # Automatically adjust x-axis range
        ax.set_ylim(y_min, y_max)  # Automatically adjust y-axis range
        ax.set_title(f"Timestep: {frame}")
        ax.legend()
        ax.set_aspect('auto')  # Ensure proper aspect ratio for the data

    ani = FuncAnimation(fig, update, frames=len(positions), interval=interval, repeat=True)
    ani.save(output_path, writer='imagemagick')
    plt.show()
