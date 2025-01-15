import numpy as np
from coverage_control.agents import generate_agents, load_agent_positions

def test_generate_agents():
    agents = generate_agents(5, seed=42)
    assert agents.shape == (5, 2)

def test_load_agent_positions():
    csv_file = 'input/agents.csv'
    timesteps, positions = load_agent_positions(csv_file)
    assert len(timesteps) == positions.shape[0]
    assert positions.shape[1] == 5
