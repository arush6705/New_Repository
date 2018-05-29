q, n = map(int, input().split())
factor = [1]*(n+1)
for i in range(2,n+1):
	for j in range(i,n+1,i):
		factor[j] += 1
m = max(factor) + 1
counter = [0]*m
for i in factor[1:]:
	counter[i] += 1
c = 1
for i,x in enumerate(counter[2:],start = 2):
	c += x
	counter[i] = c
print("\n".join(map(str,(counter[factor[int(input())] - 1] for _ in range(q)))))	
