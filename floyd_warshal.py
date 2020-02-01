V = 4
INF = 99999
def printSolution(dist): 
	print ("Following matrix shows the shortest distances between every pair of vertices")
	for i in range(V): 
		for j in range(V): 
			if(dist[i][j] == INF): 
				print "%7s" %("INF"), 
			else: 
				print "%7d\t" %(dist[i][j]), 
			if j == V-1: 
				print "" 
 
def F_Warshall(graph): 

	dist = map(lambda i : map(lambda j : j , i) , graph) 
	for k in range(V): 
 
		for i in range(V): 

			for j in range(V):  
				dist[i][j] = min(dist[i][j] , 
								dist[i][k]+ dist[k][j] 
								) 
	printSolution(dist) 


graph = [[0,5,INF,10], 
			[INF,0,3,INF], 
			[INF, INF, 0, 1], 
			[INF, INF, INF, 0] 
		] 
F_Warshall(graph); 

