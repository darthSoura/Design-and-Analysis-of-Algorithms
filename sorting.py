from bubblesort import bubblesort
from selectionsort import selectionsort
from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quicksort
from heapsort import heapsort
 
def sortByAlgo(A, algo):
    if algo == 'bubblesort':
        bubblesort(A)
    elif algo == 'selectionsort':
        selectionsort(A)
    elif algo == 'insertionsort':
        insertionsort(A)
    elif algo == 'mergesort':
        mergesort(A)
    elif algo == 'quicksort':
        quicksort(A, 0, len(A)-1)
    elif algo == 'heapsort':
        heapsort(A)
    else:
        print("Bad Algorithm") 

A = [89, 45, 68, 90, 29, 34, 17]
print("Unsorted Array: ", A)
sortByAlgo(A, 'mergesort')
print("Sorted Array: ", A)