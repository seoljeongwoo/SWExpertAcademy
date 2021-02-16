T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")
    DP = [ [-1]*71 for _ in range(71)]
    n,a,b = map(int,input().split())
    def solve(N,R):
        if R==0 or N==R: return 1
        if DP[N][R] != -1: return DP[N][R]
        DP[N][R] = solve(N-1,R) + solve(N-1,R-1)
        return DP[N][R]
    print(solve(n,a))
