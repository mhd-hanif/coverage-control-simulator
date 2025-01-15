from scipy.spatial import Voronoi

def compute_voronoi(agents):
    """
    Compute Voronoi partitions for a given set of agents.
    
    Parameters:
        agents (numpy.ndarray): An array of shape (N, 2) representing agent coordinates.
    
    Returns:
        Voronoi: A Voronoi object containing partition information.
    """
    return Voronoi(agents)
