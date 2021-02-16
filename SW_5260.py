
T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end="")
    N,K=map(int,input().split())
    result = 0
    def sum_of_subset(V,S):
        global result
        if S == 0: 
            result += 1
            return 
        if V == 0 or S < 0: return
        
        bound = S - V*(V+1)//2
        if bound <= 0 and S-V>=0: sum_of_subset(V-1,S-V)
        bound += V
        if bound <= 0 : sum_of_subset(V-1,S)
        return

    sum_of_subset(N,K)
    print(result)
