def all_divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

def efficient_all_divisors(n):
    i = 1
    while i**2<n:
        if n%i==0:
            print(i)
        i+=1
    while i>=1:
        if n%i==0:
            print(int(n/i))
        i-=1
efficient_all_divisors(int(input("Enter the number: ")))