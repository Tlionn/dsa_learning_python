def find_hcf(x,y):
    if x>y:
        if y%x==0:
            return x
        hcf = 1
        for i in range(1,int(x/2)+1):
            if x%i == 0 and y%i == 0:
                hcf = i
        return hcf
    elif y>x:
        if x%y==0:
            return y
        hcf = 1
        for i in range(1,int(y/2)+1):
            if x%i == 0 and y%i == 0:
                hcf = i
        return hcf

x,y = input("Enter the numbers separaed by space: ").split(" ")
print(find_hcf(int(x),int(y)))