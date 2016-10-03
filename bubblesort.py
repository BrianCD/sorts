from random import randrange as rand
arr = [rand(0,10000) for x in range(100)]
swapped = true
while swapped:
	swapped = false
	for i in range(len(arr)-1):
		if arr[i]>arr[i+1]:
			arr[i],arr[i+1]=arr[i+1],arr[i]
			swapped = true;
print arr