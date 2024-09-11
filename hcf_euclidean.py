def find_hcf(x,y):
    while x!=y:
        if x>y:
            x = x-y
        else:
            y= y-x
    return x

def optimized_euclidean(x,y):
    if y == 0:
        return x
    return optimized_euclidean(y,x%y)

x,y = input("Enter the numbers separaed by space: ").split(" ")
print(find_hcf(int(x),int(y)))
