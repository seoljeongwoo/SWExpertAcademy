import heapq
import copy
T = int(input())
def check(mid):
    
    new_lst = copy.deepcopy(lst)
    used = 0
    for i in range(1,N):
        if new_lst[i] - new_lst[i-1] > mid:
            gap = new_lst[i] - new_lst[i-1]
            new_lst[i] -= (gap-mid)
            used += (gap-mid)
    for i in range(N-1,0,-1):
        if new_lst[i-1] - new_lst[i] > mid:
            gap = new_lst[i-1] - new_lst[i]
            new_lst[i-1] -= (gap-mid)
            used += (gap-mid)
    return used <= K
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    N,K=map(int,input().split())
    lst = list(map(int,input().split()))
    lo,hi = 0,max(lst)+1
    result = 0
    while lo<hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid
        else:
            lo = mid+1
    print(hi)