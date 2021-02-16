from bisect import bisect_left
T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end="")
    lst = list(map(int,input().split()))[1:]
    LIS = [lst[0]]
    for i in range(1,len(lst)):
        idx = bisect_left(LIS, lst[i])
        if idx >= len(LIS): LIS.append(lst[i])
        else: LIS[idx] = lst[i]
    print(len(LIS))
