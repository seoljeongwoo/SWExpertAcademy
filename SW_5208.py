T = int(input())
for case in range(T):
    print("#{} ".format(case+1), end="")
    lst = list(map(int,input().split()))
    N ,DP = lst[0],[int(1e9)]*(lst[0]+1)
    DP[1] = -1
    for i in range(1,N):
        if DP[i] == int(1e9) : continue
        for j in range(i+1,i+lst[i]+1):
            if j > N: continue
            DP[j] = min(DP[j], DP[i] + 1)
    print(DP[N])
