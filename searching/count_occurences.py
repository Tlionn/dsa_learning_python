def search(arr,n,find_starting_index):
    answer = -1
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if n<arr[mid]:
            high = mid-1
        elif n>arr[mid]:
            low = mid+1
        else:
            answer = mid
            if find_starting_index:
                high = mid-1
            else:
                low = mid+1
    return answer

def count_occurences(arr,n):
    first = search(arr,n,True)
    last = search(arr,n,False)
    if first!=-1 and last!=-1:
        return last-first+1
    else:
        return 0
    
print(count_occurences([1,2,3],3))