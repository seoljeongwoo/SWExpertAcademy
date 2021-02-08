T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N = int(input())
    e = [list(map(int,input().split())) for __ in range(N)]
    DP = [[-1]*(1<<(N+1)) for _ in range(N)]
    def solve(curr, status):
        if (status ==  (1<<N)-1): return e[curr][0]
        if DP[curr][status] != -1: return DP[curr][status]
        DP[curr][status] = int(1e9)
        for i in range(N):
            if (1<<i)&status: continue
            DP[curr][status] = min(DP[curr][status], solve(i,status | (1<<i) )+ e[curr][i])
        return DP[curr][status]

    print(solve(0,1))