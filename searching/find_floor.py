def find_floor(A,N,X):
    low = 0
    high = N-1
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if X==A[mid]:
            return mid
        elif X<A[mid]:
            high = mid-1
        else:
            ans = mid
            low = mid+1
    return ans

