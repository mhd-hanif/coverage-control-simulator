import pandas as pd
import numpy as np

def generate_agents(n, seed=None):
    """
    Generate random agent positions in a 2D space.
    
    Parameters:
        n (int): Number of agents.
        seed (int, optional): Random seed for reproducibility.
    
    Returns:
        numpy.ndarray: Array of shape (n, 2) with agent coordinates.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.rand(n, 2)

def load_agent_positions(csv_file):
    """
    Load agent positions over time from a CSV file.
    
    Parameters:
        csv_file (str): Path to the CSV file containing agent positions.
    
    Returns:
        tuple: (timesteps, positions), where timesteps is a list of time indices,
               and positions is an array of shape (T, N, 2).
    """
    data = pd.read_csv(csv_file)
    timesteps = data['t'].values
    positions = data.drop(columns=['t']).values.reshape(len(timesteps), -1, 2)
    return timesteps, positions
