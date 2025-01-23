import numpy as np
from coverage_control.coverage_density import CoverageDensity
from coverage_control.voronoi import compute_voronoi
from coverage_control.visualization import plot_voronoi

# Initialize the coverage density grid
grid = CoverageDensity(x_min=0, x_max=10, y_min=0, y_max=10, resolution=0.1)

# Define agent positions
agent_positions = np.array([
    [2, 3],
    [6, 7],
    [4, 5],
    [8, 2]
])

# Update the density based on agents
grid.update_density(agent_positions, amplitude=0.2, decay_rate=0.3)

# Compute the Voronoi diagram
vor = compute_voronoi(agent_positions)

# Visualize the combined density, agents, and Voronoi diagram
plot_voronoi(vor, agent_positions, density=grid.density, x_min=grid.x_min, x_max=grid.x_max, y_min=grid.y_min, y_max=grid.y_max, cmap="jet")
