def binary_search(l,x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binary_search([10,20,30,40,50,60,70],60))