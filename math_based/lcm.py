def naive_lcm(a,b):
    res = max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        res+=1

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    hcf = gcd(a,b)
    return a*b//hcf

a,b = input("Enter the numbers separaed by space: ").split(" ")
print(lcm(int(a),int(b))) 