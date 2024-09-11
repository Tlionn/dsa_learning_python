def is_pal(num):
    rev = 0
    temp = num
    while temp!=0:
        last_digit = temp%10
        temp = temp//10
        rev = 10*rev + last_digit
    return rev==num

num = int(input("Enter the number to check: "))
print(is_pal(num))
