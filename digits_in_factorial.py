import math

def get_digits(n):
    if n ==0 or n ==1:
        return 1
    log_sum = 0
    for i in range(2,n+1):
        log_sum+= math.log10(i)
    return math.ceil(log_sum)

n = int(input("Enter the number for which the number of digits in its factorial is to be calculated: "))
print(get_digits(n))