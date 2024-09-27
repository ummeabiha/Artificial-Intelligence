def difference(arr):
    arr.sort()
    diff = arr[-1] - arr[0]
    print (f"Min: {arr[0]}, Max: {arr[-1]}, Difference: {diff}")
    
arr = [1, 2, 3, 4, 5, 8, 9, 10, 15, 40, 3]
difference(arr)