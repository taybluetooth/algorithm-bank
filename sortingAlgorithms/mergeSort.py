# merge sort algorithm
# worst case O(nlogn) complexity

# divide the unsorted array into subarrays each of size 1
# repeatedly merge subarrays until only one remains

# merge 2 sorted sublists A[low - mid] and A[mid + 1 - high]
def merge(A, aux, low, mid, high):

	k = low
	i = low
	j = mid + 1

	# While there are elements in the left and right runs
	while i <= mid and j <= high:

		if A[i] <= A[j]:
			aux[k] = A[i]
			k = k + 1
			i = i + 1
		else:
			aux[k] = A[j]
			k = k + 1
			j = j + 1

	# Copy remaining elements
	while i <= mid:
		aux[k] = A[i]
		k = k + 1
		i = i + 1

	# No need to copy the second half

	# copy back to the original list to reflect sorted order
	for i in range(low, high + 1):
		A[i] = aux[i]

# sort list A[low - high] using aux list
def mergeSort(A, aux, low, high):
    # best case scenario
    if high == low:
        return

    # find midpoint of list
    mid = (low + ((high - low) >> 1 ))

    # recursively split runs into two halves until run size == 1,
	# then merge them and return back up the call chain

    mergeSort(A, aux, low, mid)
    mergeSort(A, aux, mid + 1, high)

    merge(A, aux, low, mid, high)

if __name__ == '__main__':
    A = [23, 1, 2, 9, 12, -4, 2]
    aux = A.copy()

    print("Unsorted", A)
    mergeSort(A, aux, 0, len(A) - 1)
    print("Sorted", A)
