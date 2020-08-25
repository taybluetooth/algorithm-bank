# selection sort algorithm
# both worst and best case O(N^2) complexity.

# divide array into 2 subsets, sorted and unsorted.
# initially sorted is empty.
# find smallest/largest element in list.
# swap with leftmost element
# move sublist boundaries to the right.

# helper function to swap 2 indices on list.
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# selection sort function
def selectionSort(A):
    for i in range(len(A) - 1):
        # find minimum element in unsorted subset
        # and swap it with A[i]
        min = i

        for j in range(i + 1, len(A)):
            # if A[j] element is less, then it is minimum
            if A[j] < A[min]:
                # update minimum index
                min = j

            # swap minimum element in subset with A[i]
            swap(A, min, i)

if __name__ == '__main__':
    A = [-5, -10, 9, 3, 1, 12, 2]
    print("Unsorted:", A)
    selectionSort(A)
    print("Sorted:", A)
