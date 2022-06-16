def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0:
            if less(arr[j], arr[j - 1]):
                exch(arr, j, j - 1)
            else: break
            j = j - 1
            print(arr)


def exch(arr, i , j):
    a = arr[i]
    arr[i] = arr[j]
    arr[j] = a

def less(n1, n2):
    return n1 < n2 

arr = [10,5,77,7,4,3,123,44,22]

insertion_sort(arr);

