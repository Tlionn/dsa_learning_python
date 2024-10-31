def intersection(a,b,m,n):
    i = 0
    j = 0
    while i<m and j<n:
        if i>0 and a[i-1]==a[i]:
            i+=1
            continue
        if a[i]<b[j]:
            i+=1
        elif b[j]<a[i]:
            j+=1
        else:
            print(a[i], end= " ")
            i+=1
            j+=1

intersection([1,20,20,40,60],[2,20,20,20],5,4)