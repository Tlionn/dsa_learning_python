def x_to_n(x,n):
    if n ==0:
        return 1
    if n==1:
        return x
    res = x
    while n>0:
        res*=x
        n-=1
    return res

def efficient(x,n):
    if n == 0:
        return 1
    temp = efficient(x,n//2)
    temp=temp*temp
    if (n%2==0):
        return temp
    else:
        return temp*x

x,n = input("Enter the number and the power to which it should be raised seperated by a space: ").split(" ")
print(efficient(int(x),int(n)))