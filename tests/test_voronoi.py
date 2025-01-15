import numpy as np
from coverage_control.voronoi import compute_voronoi

def test_compute_voronoi():
    agents = np.array([[0.1, 0.1], [0.9, 0.1], [0.5, 0.5]])
    vor = compute_voronoi(agents)
    assert vor.points.shape == (3, 2)
