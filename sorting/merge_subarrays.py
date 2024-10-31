def merge(a,low,mid,high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    k = low
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k] = right[j]
            k+=1
            j+=1
    while i<len(left):
        a[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        a[k] = right[j]
        j+=1
        k+=1
    return a

print(merge([10,15,20,40,7,11,55],0,3,6))