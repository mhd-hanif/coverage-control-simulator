import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d

def plot_voronoi(vor, agents):
    """
    Plot the Voronoi diagram along with agent positions.
    
    Parameters:
        vor (Voronoi): Voronoi object.
        agents (numpy.ndarray): Array of shape (N, 2) with agent coordinates.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, point_size=10)
    ax.scatter(agents[:, 0], agents[:, 1], color='red', label='Agents', zorder=5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title("Voronoi Diagram")
    plt.show()
