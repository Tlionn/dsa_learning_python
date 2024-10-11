def get_smaller(A,N):
    return [ele for ele in A if ele < N]

A = [8,100,20,40,3,7]
N = 10
print(get_smaller(A,N))