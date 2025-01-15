import numpy as np
from coverage_control.agents import generate_agents
from coverage_control.voronoi import compute_voronoi
from coverage_control.visualization import plot_voronoi

# Generate agents
agents = generate_agents(5, seed=42)

# Compute Voronoi diagram
vor = compute_voronoi(agents)

# Visualize the result
plot_voronoi(vor, agents)
