def peak_element(arr,n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        elif mid>0 and arr[mid-1]>arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

print(peak_element([1,1,2,1,1],5))