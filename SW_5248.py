T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    N,M= map(int,input().split())
    lst = list(map(int,input().split()))
    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]
    def merge(u,v):
        u = find(u)
        v = find(v)
        if u==v: return
        p[u] = v
        return
    p = [ i for i in range(N+1)]
    for i in range(1,2*M,2):
        merge(lst[i],lst[i-1])
    result = 0
    for i in range(1,N+1):
        if p[i] == i: result += 1
    print(result)

