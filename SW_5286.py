def graph_color(node):
    if node == N: return True

    used = [True] * M
    for adjacent in edge[node]:
        if color[adjacent] == -1: continue
        used[color[adjacent]] = False
    
    pick = -1
    for i in range(M):
        if used[i] == True:
            pick = i
            break
    
    if pick == -1: return False
    color[node] = pick
    return graph_color(node+1)


T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    N,E,M = map(int,input().split())
    edge = [ [] for _ in range(N)]
    color = [-1]*N
    for _ in range(E):
        u,v = map(int,input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    if graph_color(0): print(1)
    else: print(0)