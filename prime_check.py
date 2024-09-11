def naive_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def efficient_prime(n):
    if n ==1:
        return False
    i = 2
    while (i**2<=n):
        if n%i==0:
            return False
        i+=1
    return True

def most_efficient(n):
    if n == 1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while (i**2<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

n= int(input("Enter the number whose primality has to be checked: "))
print(efficient_prime(n))