import math
def calculate_roots(a,b,c):
    discriminant = b*b-4*a*c
    if discriminant<0:
        return -1
    root1 = (-b+math.sqrt(discriminant))/(2*a)
    root2 = (-b-math.sqrt(discriminant))/(2*a)
    print(root1, root2)

a,b,c = input("Enter the coefficients seperated by a space: ").split()
calculate_roots(float(a),float(b),float(c))