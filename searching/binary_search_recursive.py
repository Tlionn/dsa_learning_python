def bsearch(l,x,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        return bsearch(l,x,low,mid-1)
    elif l[mid]<x:
        return bsearch(l,x,mid+1,high)

print(bsearch([10,20,30,40,50,60,70],60,0,6)) 