visited = [False for _ in range((10**5)+1)]
ap = []
mod = (10**5) + 1
adj = [[] for _ in range((10**5)+1)]
parent = [-1 for _ in range((10**5)+1)]
disc = [mod for _ in range((10**5)+1)]
low = [mod for _ in range((10**5)+1)]
def dfs(adj,disc,low,visited,parent,vertex,time):
	visited[vertex] = True
	global ap
	child = 0
	low[vertex] = disc[vertex] = time + 1
	for i in range(len(adj[vertex])):
		temp = adj[vertex][i]
		if visited[temp] == False:
			child += 1
			parent[temp] = vertex
			dfs(adj,disc,low,visited,parent,temp,time+1)
			low[vertex] = min(low[vertex],low[temp])
			if parent[vertex] == -1 and child > 1:
				ap.append(vertex)
			if 	disc[vertex] <= low[temp] and parent[vertex] != -1:
				ap.append(vertex)
		elif temp != parent[vertex]:
			low[vertex] = min(low[vertex],disc[temp])



n,e = map(int,input().split())
for _ in range(e):
	a,b = map(int,input().split())
	adj[a].append(b)
	adj[b].append(a)
dfs(adj,disc,low,visited,parent,0,0)
print(ap)
