from coverage_control.agents import load_agent_positions
from coverage_control.animation import animate_voronoi

# Load agent positions from the CSV file
csv_file = 'input/agents.csv'  # Path to the CSV file
timesteps, positions = load_agent_positions(csv_file)

# Create and save the dynamic Voronoi animation
animate_voronoi(positions, 'output/dynamic_voronoi_example.gif', fps=20)
