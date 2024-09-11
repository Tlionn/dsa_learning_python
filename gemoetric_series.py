def power(r,n):
    if n==0:
        return 1
    temp = power(r,n//2)
    temp = temp*temp
    if n%2==0:
        return temp
    else:
        return temp*r

def term_of_gp(A,B,N):
    if N==1:
        return A
    r = B/A
    r_power = power(r,N-1)
    term = A*r_power
    return term

A,B,N = input("Enter A, B and N seperated by spaces: ").split()
print(term_of_gp(int(A),int(B),int(N)))