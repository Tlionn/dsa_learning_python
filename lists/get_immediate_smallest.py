def immediate_smallest(arr,x):
    smallest = [a for a in arr if a < x]
    smallest.sort()
    return smallest[-1] if smallest else -1
arr = [1,2,3,4,5]
x = 1
print(immediate_smallest(arr,x))