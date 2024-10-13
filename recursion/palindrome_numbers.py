def helper(N,rev):
    if N==0:
        return rev
    rev = rev*10+N%10
    return helper(N//10,rev)

def isPalin(N):
    return N == helper(N,0)

print(isPalin(101))    