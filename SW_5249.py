import heapq
T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")
    N,M= map(int,input().split())
    def find(u):
        if u!= p[u]:
            p[u] = find(p[u])
        return p[u]

    def merge(u,v):
        u=find(u)
        v=find(v)
        p[u] =v
        return

    pq , p = [] , [i for i in range(N+1)]
    for _ in range(M):
        u,v,w = map(int,input().split())
        heapq.heappush(pq, (w,u,v))
    result = 0 
    while pq:
        w,u,v = heapq.heappop(pq)
        if find(u) == find(v) : continue
        merge(u,v)
        result += w
    print(result)
