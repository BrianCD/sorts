from random import randrange as rand
arr = [rand(0,10000) for x in range(100)]
for x in range(len(arr)/2):
	a = len(arr)-x-1
	min, minindex = arr[x],x
	max, maxindex = arr[a],a
	for y in range(x+1, len(arr)):
		if (min > arr[y]):
			min = arr[y]
			minindex = y
		if (max < arr[y]):
			max = arr[y]
			maxindex = y
	arr[x],arr[minindex] = arr[minindex],arr[x]
	arr[a],arr[maxindex] = arr[maxindex],arr[a]
print arr