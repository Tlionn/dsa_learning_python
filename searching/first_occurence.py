def first_occurence(l,x):
    low = 0
    high = len(l) - 1
    while low<=high:
        mid = (low+high)//2
        if x>l[mid]:
            low = mid+1
        elif x<l[mid]:
            high = mid-1
        else:
            if mid == 0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high = mid-1
    return -1

print(first_occurence([5,10,10,20,20],20)) 