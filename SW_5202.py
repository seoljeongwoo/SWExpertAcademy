T= int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N =int(input())
    lst = []
    for __ in range(N):
        a,b = map(int,input().split())
        lst.append((b,a))
    lst.sort()
    en,count=0,1
    for i in range(1,N):
        if lst[en][0] <= lst[i][1]:
            count +=1
            en = i
    print(count)