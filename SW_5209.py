T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    DP = [[-1]*(1<<N) for _ in range(N)]
    def solve(curr, state):
        if state == 2**N -1 : return 0
        if DP[curr][state] != -1: return DP[curr][state]
        DP[curr][state] = int(1e9)
        for i in range(N):
            if state & (1<<i) : continue
            DP[curr][state] = min(DP[curr][state] , solve(curr+1 , state|(1<<i)) + lst[curr][i])
        return DP[curr][state]
    print(solve(0,0))