"""
This program finds a number in a list that is immediately greater than the given value
"""

def immediate_greater(arr,x):
    greatest = [a for a in arr if a > x]
    greatest.sort()
    return greatest[0] if greatest else -1

arr = [4,67,13,12,15]
x = 16

print(immediate_greater(arr,x))