from collections import deque
T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case) , end="")
    N,M= map(int,input().split())
    def bfs(st, target):
        q = deque()
        visited = [-1] * (int(1e6)+1)
        q.append(st)
        visited[st] = 0
        while q:
            curr = q.popleft()
            if curr == target:
                return visited[curr]
            
            if curr+1 <=int(1e6) and visited[curr+1] == -1 :
                q.append(curr+1)
                visited[curr+1] = visited[curr] + 1
            if curr-1 > 0 and visited[curr-1] == -1:
                q.append(curr-1)
                visited[curr-1] = visited[curr] + 1
            if curr*2 <= int(1e6) and visited[curr*2] == -1:
                q.append(curr*2)
                visited[curr*2] = visited[curr] + 1
            if curr-10> 0 and visited[curr-10] == -1:
                q.append(curr-10)
                visited[curr-10] = visited[curr] + 1
        
    print(bfs(N,M))