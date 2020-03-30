import snap

G1 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)


num_nodes = 0
for _ in G1.Nodes():
    num_nodes += 1
print("The number of nodes:", num_nodes)


num_self_edges = 0
for edge in G1.Edges():
    if edge.GetSrcNId() == edge.GetDstNId():
        num_self_edges += 1
print("The number of self loops:", num_self_edges)


num_directed_edges = 0
for edge in G1.Edges():
    if edge.GetSrcNId() != edge.GetDstNId():
        num_directed_edges += 1
print("The number of directed edges:", num_directed_edges)


num_undirected_edges = 0
edges_found = set()
for edge in G1.Edges():
    u, v = edge.GetSrcNId(), edge.GetDstNId()
    if u > v:
        u, v = v, u
    ordered_edge = (u, v)
    if ordered_edge not in edges_found:
        num_undirected_edges += 1
    edges_found.add(ordered_edge)
print("The number of undirected edges:", num_undirected_edges)


num_reciprocated_edges = 0
edges_found = set()
for edge in G1.Edges():
    u, v = edge.GetSrcNId(), edge.GetDstNId()
    if u > v:
        u, v = v, u
    ordered_edge = (u, v)
    if ordered_edge in edges_found:
        num_reciprocated_edges += 1
    else:
        edges_found.add(ordered_edge)
print("The number of reciprocated edges:", num_reciprocated_edges)


num_zero_indegree = 0
num_zero_outdegree = 0
num_over_10_outdegree = 0
num_below_10_indegree = 0
for node in G1.Nodes():
    if node.GetOutDeg() == 0:
        num_zero_outdegree += 1
    if node.GetInDeg() == 0:
        num_zero_indegree += 1
    if node.GetOutDeg() > 10:
        num_over_10_outdegree += 1
    if node.GetInDeg() < 10:
        num_below_10_indegree += 1
print("Number of nodes with zero out-degree:", num_zero_indegree)
print("Number of nodes with zero in-degree", num_zero_indegree)
print("Number of node with out-degree larger than 10", num_over_10_outdegree)
print("Number of ndoes with in-degree lower than 10:", num_below_10_indegree)
