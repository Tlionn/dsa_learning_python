"""
Semi efficient method
"""
def get_prime_numbers(n):
    if n<2:
        print("No prime numebrs")
    if n==2:
        print(n)
    if n==3:
        print("2,3")
    if n>3:
        print(2)
        print(3)
    i = 5
    while i<=n:
        print(i)
        if i+2<=n:
            print(i+2)
        i+=6

get_prime_numbers(int(input("Enter the number: ")))