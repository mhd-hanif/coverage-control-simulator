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
