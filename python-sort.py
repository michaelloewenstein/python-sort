import math

class SortManager(object):

	@staticmethod
	def quickSort(arr,left,right):
		if(left<right):
			p = SortManager.partition(arr,left,right)
			SortManager.quickSort(arr, left, p-1)
			SortManager.quickSort(arr, p+1, right)

	@staticmethod
	def choosePivot(arr, left, right):
		pivot = left + (right - left) // 2
		return pivot
	@staticmethod
	def partition(arr,left,right):
		pivotIndex = SortManager.choosePivot(arr,left,right)		
		pivotValue = arr[pivotIndex]
		arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
		currentIndex = left
		for index in range(left,right):
			if(arr[index] < pivotValue):
				arr[currentIndex],arr[index] = arr[index], arr[currentIndex]
				currentIndex = currentIndex + 1
		arr[currentIndex], arr[right] = arr[right], arr[currentIndex]

		return currentIndex

	@staticmethod
	def swap(left,right):
		return right,left
	
arr = [2,3,4,6,1,9]
SortManager.quickSort(arr,0,5)		
print(arr)
