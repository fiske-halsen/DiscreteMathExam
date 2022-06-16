def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if less(arr[j], arr[min]):
                min = j
        exch(arr, i , min)
    print(arr)  

def exch(arr, i , j):
    a = arr[i]
    arr[i] = arr[j]
    arr[j] = a

def less(n1, n2):
    return n1 < n2 

arr = [10,5,77,7,4,3,123,44,22]

selection_sort(arr)




