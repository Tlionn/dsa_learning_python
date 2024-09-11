def get_trailing_zeroes(n):
    if n <0:
        return -1
    count = 0
    i = 5
    while n // i > 1:
        count+= n // i
        i*=5
    return count

n = int(input("Enter the number fo which the number of trailing zeroes in its factorial is to be found: "))
print(get_trailing_zeroes(n))