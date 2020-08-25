# insertion sort algorithm
# worst case O(N^2) complexity
# best case O(N) complexity (when array is sorted)

# algorithm divides array into 2 subsets.
# sorted subset consists of one element initially.
# each iteration removes element from unsorted array and places into sorted.
# repeat until no unsorted elements remain.

# insertion sort function.

def insertionSort(A):

    # start from 2nd element as first is already sorted

    for i in range(1, len(A)):
        value = A[i]
        j = i

        # find index j in sorted subset where the number in unsorted belongs

        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1

        # assign new value to sorted subset

        A[j] = value

if __name__ == '__main__':
    A = [-2, 4, 1, 9, 21, 2, 41]
    print("Unsorted:", A)
    insertionSort(A)
    print("Sorted:", A)
