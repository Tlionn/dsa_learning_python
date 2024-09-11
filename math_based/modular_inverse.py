def mod_inverse(a,m):
    for i in range(1,m+1):
        if (a*i)%m==1:
            return i
    return -1
    
a,m = input("Enter the number and module values seperated by a space: ").split()
print(mod_inverse(int(a),int(m)))