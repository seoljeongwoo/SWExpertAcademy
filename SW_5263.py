import copy
T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")

    result = -987654321
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i!=j and lst[i][j] == 0: lst[i][j] = float('inf')

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i==k or i==j or j==k: continue
                if lst[i][j] > lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
    for x in lst:
        result = max(result, max(x))
    print(result)