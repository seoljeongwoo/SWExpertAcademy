T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end="")
    DP = [-1]*31
    def solve(n):
        if n==0 or n==1 : return 1
        elif n==2: return 3
        elif n==3: return 6

        if DP[n] != -1: return DP[n]
        DP[n] = solve(n-1) + 2*solve(n-2) + solve(n-3)
        return DP[n]
    N = int(input())
    print(solve(N))