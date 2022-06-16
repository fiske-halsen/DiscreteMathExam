
def linear_search(arr, x):
 
    for i in range(len(arr)): # Scanning each elements (Full scan)
 
        if arr[i] == x:
            return i
 
    return -1



arr = [1,4,5,7,9,12,15,18,19,22,23,25,29,30,33,35,40,41,50]

print(linear_search(arr, 35));