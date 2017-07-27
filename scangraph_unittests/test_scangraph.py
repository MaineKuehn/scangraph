import scangraph.scangraph
from graphi.types.adjacency_graph import AdjacencyGraph

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestScanGraph(unittest.TestCase):
    clusterer_cls = scangraph.scangraph.ScanGraph

    def test_creation(self):
        graph = AdjacencyGraph({
            1: {2: .5, 3: .5, 4: .5, 7: .5},
            2: {1: .5},
            3: {1: .5, 7: .5},
            4: {1: .5, 5: .5, 6: .5},
            5: {4: .5, 6: .5},
            6: {4: .5, 5: .5},
            7: {1: .5, 3: .5}
        }, undirected=True)
        clusterer = self.clusterer_cls(base_graph=graph, minimum_distance=None, minimum_neighbours=3)
        self.assertIsNotNone(clusterer)
