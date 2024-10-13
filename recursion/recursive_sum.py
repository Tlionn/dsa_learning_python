def recursiveSum(n):
    #code here
    if n==0:
        return 0
    return n+recursiveSum(n-1)

print(recursiveSum(5))