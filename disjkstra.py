import heapq
adj = [[] for _ in range((10**5)+1)]
vis = [False]*((10**5)+1)
dis = [10**5]*((10**5)+1)
def disjastra():
	arr = [(0,1)]
	dis[1] = 0
	heapq.heapify(arr)
	#heapq.heappush()
	#heapq.heappop(arr)
	while len(arr) != 0:
		temp = heapq.heappop(arr)
		if vis[temp[1]] == True:
			continue
		x = temp[1]
		wt = temp[0]
		vis[x] == True	
		for i in range(len(adj[x])):
			if dis[adj[x][i][0]] > wt + adj[x][i][1]:
				dis[adj[x][i][0]] = wt + adj[x][i][1]
				heapq.heappush(arr,(dis[adj[x][i][0]],adj[x][i][0]))


n,e = map(int,input().split())
for _ in range(e):
	a,b,wt = map(int,input().split())
	adj[a].append((b,wt))
	adj[b].append((a,wt))
disjastra()	
for i in range(1,n+1):
	print(dis[i])
