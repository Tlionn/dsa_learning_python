def selectosort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if arr[j]< arr[min_ind]:
                min_ind = j
        arr[min_ind],arr[i] = arr[i], arr[min_ind]
    return arr

print(selectosort([10,8,20,5]))