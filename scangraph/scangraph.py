from graphi.abc import Graph
from scangraph.cluster import Cluster


class ScanGraph(Graph):
    def __init__(self, base_graph, minimum_distance, minimum_neighbours):
        if not base_graph.undirected:
            raise ValueError("undefined behaviour for directed graphs")
        self.graph = base_graph
        self.minimum_distance = minimum_distance
        self.minimum_neighbours = minimum_neighbours
        self.clusters = {}
        self.cores = {}
        self._cluster()

    def _cluster(self):
        for node in self.graph:
            neighbours = list(self.neighbourhood(node, distance=self.minimum_distance))
            if len(neighbours) >= self.minimum_neighbours:
                # found a new core node
                cluster = Cluster(name=len(self.clusters))
                self.cores[node] = cluster.name
                cluster.add(node, state=Cluster.CORE_NODE)
                for neighbour in neighbours:
                    try:
                        cluster_id = self.cores[neighbour]
                    except KeyError:
                        cluster.add(neighbour, Cluster.BORDER_NODE)
                    else:
                        # merge clusters
                        cluster += self.clusters[cluster_id]
                        self.clusters[cluster_id] = cluster
                self.clusters[cluster.name] = cluster
                # TODO: communicate core state for node
        for cluster in set(self.clusters.values()):
            print(cluster)

    def update(self, other):
        pass

    def neighbourhood(self, node, distance=None):
        # first check local count of neighbours
        local_neighbours = self.graph.neighbourhood(node, distance=distance)
        # if local neighbourhood is not sufficient, also return remote neighbourhood
        return local_neighbours

    def clear(self):
        pass

    def copy(self):
        pass

    def __delitem__(self, item):
        pass

    def __setitem__(self, item, value):
        pass

    def __getitem__(self, item):
        pass

    def __iter__(self):
        pass

    def add(self, node):
        pass
