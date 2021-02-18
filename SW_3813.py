TC = int(input())
def check(mid):
    cnt = 0 
    j = 0 
    for i in range(N):
        if j == K: break
        if lst[i] <= mid:
            cnt += 1
            if cnt == wear[j]:
                j+=1
                cnt = 0
        else:
            cnt = 0

    return j==K
for case in range(1,TC+1):
    print("#{} ".format(case), end="")
    N,K= map(int,input().split())
    lst = list(map(int,input().split()))
    wear = list(map(int,input().split()))
    lo ,hi = 0, max(lst)+1
    while lo<=hi:
        mid = (lo+hi)//2
        if check(mid): 
            hi = mid-1
        else:
            lo = mid+1
    print(lo)