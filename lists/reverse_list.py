def reverse(l):
    l_new = []
    for i in range(1,len(l)+1):
        l_new.append(l[-i])
    return l_new

def swap_to_reverse(l):
    s = 0
    e = len(l)-1
    while s<e:
        l[s],l[e] = l[e],l[s]
        s += 1
        e -= 1
    return l
print(swap_to_reverse([1,2,3]))