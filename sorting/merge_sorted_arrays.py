def merge(a,b):
    m = len(a)
    n = len(b)
    res = []
    i, j = 0,0
    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1
    return res

print(merge([10,15],[5,6,6,30,40]))