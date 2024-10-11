def rotatearr(arr,d):
    n = len(arr)
    x = arr[:d]
    for i in range(d,n):
        arr[i-d] = arr[i]
    arr[n-d:] = x
    return arr

print(rotatearr([1,2,3,4],2))