def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0 
	for i in range (1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
Smallest_index = findSmallest([9456456,45658,45613215,1561232,5156155,123,453213])
print(Smallest_index)
def selectionSort(arr):
	newArr = []
	arr_copy = list(arr)
	for i in range (len(arr_copy)):
		smallest = findSmallest(arr_copy)
		newArr.append(arr_copy.pop(smallest))
	return newArr, arr_copy, arr
print(selectionSort([9456456,45658,45613215,1561232,5156155,123,453213]))