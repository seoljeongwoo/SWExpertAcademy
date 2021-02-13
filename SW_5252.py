T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end= "")
    N,M= map(int,input().split())
    A,B = [input() for _ in range(N)] , [input() for _ in range(M)]
    result = 0 
    for A_string in A:
        for B_string in B:
            if A_string == B_string :
                result += 1
                break
    print(result) 