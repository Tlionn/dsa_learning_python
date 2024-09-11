def is_prime(n):
    if n==1:
        return False
    if n==2 or n ==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i**2<=n:
        if n%i == 0 or n%(i+2)==0:
            return False
        i+=6
    return True

def exactly3divisors(n):
    total = 0
    for i in range(2,int(n**(0.5))+1):
        if is_prime(i) and i**2<=n:
            total+=1
            print(i)
    return total

N = int(input("Enter the number: "))
print(f"Count of numbers with exactly 3 divisors: {exactly3divisors(N)}")