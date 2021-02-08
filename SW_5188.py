import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N= int(input())
    lst = [list(map(int,input().split())) for __ in range(N)]
    dp = [[-1]*N for __ in range(N)]
    def solve(x,y):
        if x==N-1 and y==N-1: return lst[x][y]
        if x==N or y==N: return int(1e9)
        if dp[x][y] != -1: return dp[x][y]
        dp[x][y] = min(solve(x+1,y),solve(x,y+1))
        dp[x][y] += lst[x][y]
        return dp[x][y]
    print(solve(0,0))
    
