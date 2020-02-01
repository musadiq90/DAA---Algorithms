prnt = dict()
rank = dict()

def make_set(ver):
    prnt[ver] = ver
    rank[ver] = 0

def find(ver):
    if prnt[ver] != ver:
        prnt[ver] = find(prnt[ver])
    return prnt[ver]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            prnt[root2] = root1
	else:
	    prnt[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1
def kruskal(graph):

    for ver in graph['vertices']:
	make_set(ver)
	minimum_spanning_tree = set()
	edges = list(graph['edges'])
	edges.sort()

    for edg in edges:
	weight, vertice1, vertice2 = edg

	if find(vertice1) != find(vertice2):
	    union(vertice1, vertice2)
	    minimum_spanning_tree.add(edg)
	   
    return sorted(minimum_spanning_tree)

graph = {

'vertices': ['R', 'S', 'T', 'U', 'V', 'W', 'X'],

'edges': set([

(7, 'R', 'S'),

(5, 'R', 'U'),

(7, 'S', 'R'),

(8, 'S', 'T'),

(9, 'S', 'U'),

(7, 'S', 'V'),

(8, 'T', 'S'),

(5, 'T', 'V'),

(5, 'U', 'R'),

(9, 'U', 'S'),

(7, 'U', 'V'),

(6, 'U', 'W'),

(7, 'V', 'S'),

(5, 'V', 'T'),

(15, 'V', 'U'),

(8, 'V', 'W'),

(9, 'V', 'X'),

(6, 'W', 'U'),

(8, 'W', 'V'),

(11, 'W', 'X'),

(9, 'X', 'V'),

(11, 'X', 'W'),

])

}


print kruskal(graph)