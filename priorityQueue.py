import sys
import copy
import math
def read(typ=str):
    return list(map(typ,sys.stdin.readline().split()))

def maximum(arr):
	return arr[1]

def extract_maximum(arr):
	if len(arr) == 0:
		return -1
	maxElement = arr[1]
	print('maxElement=',maxElement)
	n = len(arr) - 1
	arr[1] = arr[n]
	n = n - 1
	max_heapify(arr,1,n)
	return maxElement

def increase_val(arr,i,val):
	if arr[i] > val:
		return 
	arr[i] = val
	
	while i > 1 and arr[i//2] < arr[i]:
		swap(arr,i//2,i)
		i = i//2

def insert_val(arr,val):
	n = len(arr) 
	arr.append(-1)

	increase_val(arr,n,val)

def swap(arr,a,b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp
def max_heapify(arr,i,n):	
	left = 2*i
	right = (2*i)+1
	if left <= n and arr[left] > arr[i]:
		largest = left
	else:
		largest = i
	if right <= n and arr[right] > arr[largest]:
		largest = right
		
	if largest != i:
		swap(arr,i,largest)
		max_heapify(arr,largest,n)

def min_heapify(arr,i,n):	
	left = 2*i
	right = (2*i)+1
	#print(i)
	if left <= n and arr[left] < arr[i]:
		smallest = left
	else:
		smallest = i
	if right <= n and arr[right] < arr[smallest]:
		smallest = right
		
	if smallest != i:
		#print(arr[i],arr[smallest])
		swap(arr,i,smallest)

		min_heapify(arr,smallest,n)


def build_maxheap(arr):
	n = len(arr) - 1
	for i in range(int(n/2),0,-1):
		max_heapify(arr,i,n)

arr = [-1,1,3,4,7,8]
build_maxheap(arr)
print(arr)
insert_val(arr,6)
print(arr)
ext = extract_maximum(arr)
print(ext)
print(arr)
'''heap_size = len(arr) - 1
for i in range(len(arr)-1,1,-1):
	swap(arr,i,1)
	heap_size -= 1
	print(arr[i])
	max_heapify(arr,1,heap_size)
'''



