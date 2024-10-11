import math
def median(A,N):
    A.sort()
    if N%2==0:
        med = math.floor((A[int(N/2)]+A[int(N/2-1)])/2)
        return med
    else:
        return A[N//2]
def mean(A,N):
    return sum(A)//len(A)

N = 4
A = [2,8,3,4]
print(median(A,N), mean(A,N))