def sqrt(x):
    low = 1
    high = x
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if mid*mid==x:
            return mid
        elif mid*mid>x:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans

print(sqrt(24))
