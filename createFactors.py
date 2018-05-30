size = 10**6 + 1
mod = 10**9  + 7
dp = [0 for _ in range(size)]
valid = [False for _ in range(size)]

n = int(input())
maxx = 0
for _ in range(n):
	t = int(input())
	valid[t] = True
	maxx = max(t,maxx)
for i in range(2,size):
	if valid[i]:
		dp[i] = 1
valid[1] = False
for i in range(2,maxx+1):
	if valid[i]:
		for j in range(i+i,maxx+1,i):
			if (j // i)  <= i:
				if valid[j]:
					dp[j] = (dp[j] + (dp[i]*dp[j//i])%mod)%mod
					if i != (j//i):
						dp[j] = (dp[j] + (dp[i]*dp[j//i])%mod)%mod

ans = 0
for i in range(2,maxx+1):
	ans = (ans + dp[i])%mod
print(ans)	

#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/kala-set/description/
