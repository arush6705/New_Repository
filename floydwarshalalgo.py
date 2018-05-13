dis = [[10**5]*100 for _ in range((10**5)+1)]
n,e = map(int,input().split())
for _ in range(e):
	a,b,wt = map(int,input().split())
	dis[a][b] = wt
	dis[b][a] = wt
for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
print(dis[1][4])
