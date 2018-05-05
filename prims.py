import heapq
adj = [[] for _ in range((10*5)+1)]
visited = [0 for _ in range((10*5)+1)]
def prims(x):
	li = [(0,x)]
	heapq.heapify(li)
	minCost = 0
	while len(li) != 0:
		p = heapq.heappop(li)
		y = p[1]
		if visited[y] != 0:
			continue
		minCost += p[0]
		visited[y] = 1
		for i in range(len(adj[y])):
			d = adj[y][i][1]
			if visited[d] == 0:
				heapq.heappush(li,adj[y][i])
	return minCost


n,e = map(int,input().split())
for _ in range(e):
	x,y,wt = map(int,input().split())
	adj[x].append((wt,y))
	adj[y].append((wt,x))

print(prims(1))
