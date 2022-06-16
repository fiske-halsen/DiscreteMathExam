import math

def binary_search(arr, target):
    if not len(arr):
        return -1

    left = 0
    right = len(arr)

    while (left + 1 < right):
        mid = math.ceil((right + left) // 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            left = mid 
        else:
            right = mid

    if arr[left] == target:
        return left 

    return -1


arr = [1,4,5,7,9,12,15,18,19,22,23,25,29,30,33,35,40,41,50]


print(binary_search(arr, 35));
