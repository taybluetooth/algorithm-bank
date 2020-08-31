# quick sort algorithm
# best case O(nlogn) complexity
# worst case O(n^2) complexity

# divide and conquer algorithm with 3 distinct steps
# pivot selection (usually left or rightmost element)
# reorder array so all elements less than pivot on left, etc
# recursively apply until sorted

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(a, start, end):

    pivot = a[end]

    pIndex = start

    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1

    swap(a, end, pIndex)

    return pIndex

def quicksort(a, start, end):

    if start >= end:
        return

    pivot = partition(a, start, end)

    quicksort(a, start, pivot-1)
    quicksort(a, pivot+1, end)

if __name__ == '__main__':

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    print("Unsorted:", a)
    quicksort(a, 0, len(a) - 1)
    print("Sorted:", a)
