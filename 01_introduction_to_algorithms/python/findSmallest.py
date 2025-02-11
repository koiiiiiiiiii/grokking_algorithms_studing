def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0 
	for i in range (1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
Smallest_index = findSmallest([9456456,45658,45613215,1561232,5156155])
print(Smallest_index)
def selectionSort(arr):
	newArr = []
	for i in range (len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr
print(selectionSort([9456456,45658,45613215,1561232,5156155]))