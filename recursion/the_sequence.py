def theSequence(n):
    if n == 0:
        return 1
    return n+theSequence(n-1)*n

print(theSequence(3))