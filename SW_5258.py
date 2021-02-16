T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end = "")
    N,M= map(int,input().split())
    item , DP = [], [[0]*(N+1) for _ in range(M+1)]
    for _ in range(M):
        item.append(tuple(map(int,input().split())))
    for i in range(1,M+1):
        for j in range(0,N+1):
            if j < item[i-1][0]: DP[i][j] = DP[i-1][j]
            else: DP[i][j] = max(DP[i-1][j] , DP[i-1][j-item[i-1][0]] + item[i-1][1])
    print(DP[M][N])
