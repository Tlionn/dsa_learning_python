import numpy as np
def greatest(l):
    max = -np.inf
    if not l:
        return -1
    for ele in l:
        if ele > max:
            max = ele
    return max

def greatest_sort(l):
    if not l:
        return -1
    l.sort()
    return l[-1]

l = [10,5,20,8]
print(greatest(l))
print(greatest_sort(l))