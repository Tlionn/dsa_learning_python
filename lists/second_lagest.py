"""
Program to get the second largest number from a list in O(n) time, traversing the list only once.
"""
def get_sec_largest(l):
    if len(l)==1:
        return None
    lar = l[0]
    slar = None
    for x in l:
        if x>lar:
            slar = lar
            lar = x
        elif x!=lar:
            if slar==None or x>slar:
                slar = x
    return slar

l = [78, 20, 20, 20]
print(get_sec_largest(l))
