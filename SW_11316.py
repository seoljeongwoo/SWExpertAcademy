T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    s,p,q,m = map(int,input().split())
    dic = [-1] * m
    dic[s] = 0
    pick = 1
    while True:
        new_s = (p*s+q)%m
        if dic[new_s] == -1: 
            dic[new_s] = pick
            pick+=1
        else:
            print(pick-dic[new_s])
            break
        s= new_s
    