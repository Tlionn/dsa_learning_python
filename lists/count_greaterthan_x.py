"""
This program returns the number of elements in a list greater than a given value.
"""

def get_count(arr,x):
    return len([e for e in arr if e>x])
arr = [4,5,3,1,2]
x = 3
print(get_count(arr,x))