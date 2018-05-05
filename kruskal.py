def root(x):
	while(idx[x] != x):
		idx[x] = idx[idx[x]]
		x = idx[x]
	return x	

def union1(p,q):
	x = root(p)
	y = root(q)
	idx[x] = y

def kruskal(adj):
	minCost = 0
	for i in range(len(adj)):
		x = adj[i][1][0]
		y = adj[i][1][1]
		wt = adj[i][0]
		#print(x,y,root(x),root(y))

		if root(x) != root(y):
			minCost += wt
			union1(x,y)
	return minCost		

adj = []
idx = [i for i in range(10**5)]
n,m = map(int,input().split())
for _ in range(m):
	a,b,w = map(int,input().split())
	adj.append((w,(a,b)))

adj.sort()

print(kruskal(adj))
