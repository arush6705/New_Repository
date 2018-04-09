import sys
import copy
import math
def read(typ=str):
    return list(map(typ,sys.stdin.readline().split()))

def root(a):
	while 1:
		if (arr[a] == a):
			return a
		arr[a] = arr[arr[a]]
		a =  arr[a]

def union(x,y):
	a = root(x)
	b = root(y)
	if a == b:
		return
	if size[a] < size[b]:
		arr[a] = arr[b]
		size[b] += size[a]
	else:
		arr[b] = arr[a]
		size[a] += size[b]

def deunion(root_a):
	for i in range(1,len(arr)):
		if arr[i] == root_a:
			arr[i] = -1
def calcEdges(x):
	calc = 1
	for i in range(1,x+1):
		calc *= i
		if calc >= MOD:
			calc %= MOD
	return calc
#arr = [-1]
#size = [-1]
n,m = map(int,input().split()) 
arr = [i for i in range(n)]
size = [1]*n
MOD = 10**9+7

seive = [0 for i in range(10**5+7)]
for _ in range(m):
	x,y = map(int,input().split())
	union(x,y)
for i in range(n):
	arr[i] = root(i)
temp = 1
for i in range(n):
	t = root(i)
	if seive[t] == 0 and size[t] != 1:
		seive[t] = 1
		print(calcEdges(size[t]))
		temp *= calcEdges(size[t])
		temp %= MOD
print(temp)







