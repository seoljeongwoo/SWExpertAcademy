T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    N = int(input())
    A = [0] * (N+1)
    for _ in range(1,N+1):
        A[_] = int(input())
    for i in range(1,N+1):
        if A[i-1] + A[i] > A[i]: A[i] += A[i-1] 
    A.pop(0)
    print(max(A))