scangraph - Density-based Graph Clustering
==========================================

ScanGraph is based on concepts from DBSCAN as well as DenGraph.
However, ScanGraph tries to simplify existing concepts with a linear scan of nodes and their neighbourhoods.
The neighbourhood of a node is defined by the *number* of reachable nodes within a given *distance*.
Therefore, large groups of items which are close to each other form clusters.
As already accomplished by DenGraph, ScanGraph treats isolated, distinct and uncommon items as noise.

