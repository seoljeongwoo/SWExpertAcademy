T =int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N,M=map(int,input().split())
    container , truck = list(map(int,input().split())) , list(map(int,input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    i,j,result=0,0,0
    while i<len(container) and j<len(truck):
        if truck[j] >= container[i]:
            result += container[i]
            i+=1;j+=1
        else: i+=1
    print(result)
