import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d

def plot_voronoi(vor, agents, density=None, x_min=None, x_max=None, y_min=None, y_max=None, cmap="jet"):
    """
    Plot the Voronoi diagram along with agent positions and optionally a coverage density heatmap.

    Parameters:
        vor (Voronoi): Voronoi object.
        agents (numpy.ndarray): Array of shape (N, 2) with agent coordinates.
        density (numpy.ndarray, optional): 2D grid of coverage density values.
        x_min, x_max, y_min, y_max (float, optional): Bounds for the density heatmap.
        cmap (str): Colormap for the density heatmap.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot density heatmap if provided
    if density is not None and x_min is not None and x_max is not None and y_min is not None and y_max is not None:
        extent = [x_min, x_max, y_min, y_max]
        ax.imshow(density, extent=extent, origin="lower", cmap=cmap, interpolation="nearest")

    # Plot Voronoi diagram
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors="blue", line_width=1)

    # Plot agent positions
    ax.scatter(agents[:, 0], agents[:, 1], color="red", label="Agents", zorder=5)

    # Add labels and legend
    ax.set_title("Voronoi Diagram with Agents")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    # Add colorbar for density
    if density is not None:
        plt.colorbar(ax.imshow(density, extent=extent, origin="lower", cmap=cmap), label="Coverage Density")

    plt.show()
