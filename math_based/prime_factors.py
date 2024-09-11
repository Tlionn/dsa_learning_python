"""
Naive approach only, no optimizations
"""

def isPrime(x):
    if x == 1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    i = 5
    while i**2<=x:
        if x%i==0 or x%(i+2)==0:
            return False
        i+=6
    return True

def print_prime_factors(n):
    for i in range(2,n+1):
        if isPrime(i):
            x = i
            while n%x==0:
                print(i)
                x*=i
n = int(input("Enter the value of n: "))
print_prime_factors(n)