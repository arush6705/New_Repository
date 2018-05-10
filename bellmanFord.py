dis = [10**5 for _ in range((10**5)+1)]
arr = []
n,m = map(int,input().split())
for _ in range(m):
	a,b,wt = map(int,input().split())
	arr.append((a,b,wt))
	arr.append((b,a,wt))
dis[1] = 0
for i in range(n+1):
	for j in range(len(arr)):
		#print(arr[j][1],arr[j][0],dis[arr[j][1]],dis[arr[j][0]] + arr[j][2])
		if dis[arr[j][1]] > dis[arr[j][0]] + arr[j][2]:
			dis[arr[j][1]] = dis[arr[j][0]] + arr[j][2]
for i in range(1,n+1):
	print(dis[i])
