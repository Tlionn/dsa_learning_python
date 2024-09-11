def power(x,n):
    res = 1
    while n>0:
        if n%2!=0:
            res=res*x
        x = x*x
        n = n//2
    return res

x,n = input("Enter the values of x and n seperated by a space: ") .split()
print(power(int(x),int(n)))