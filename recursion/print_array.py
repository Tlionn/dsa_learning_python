def print_array(arr,n):
    if n==0:
        return
    print_array(arr,n-1)
    print(arr[n-1])

print_array([1,2,3,4,5],5)