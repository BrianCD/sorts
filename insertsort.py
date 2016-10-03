from random import randrange as rand
arr = [rand(0,10000) for x in range(100)]
for x in range(len(arr)):
	target = 0
	curr = arr[x]
	for y in range(x,0,-1):
		if arr[y-1]>curr:
			arr[y]=arr[y-1]
		else:
			target = y
			break
	arr[target] = curr
print arr