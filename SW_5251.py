import heapq
T= int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end="")
    N,M=map(int,input().split())
    def dijkstra(st,en):
        dist = [int(1e9)] * (N+1)
        pq= []
        heapq.heappush(pq,(0,st))
        while pq:
            curr_dist , curr = heapq.heappop(pq)
            if curr == en: return curr_dist

            if dist[curr] != int(1e9) : continue
            dist[curr] = curr_dist

            for next_vertex, weight in edge[curr]:
                if dist[next_vertex] != int(1e9) : continue
                heapq.heappush(pq, (curr_dist + weight , next_vertex))
        return -1
    edge = [ [] for _ in range(N+1)]
    for _ in range(M):
        u,v,w = map(int,input().split())
        edge[u].append((v,w))
    print(dijkstra(0,N))