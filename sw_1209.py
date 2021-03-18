import sys
input = sys.stdin.readline
for _ in range(10):
    tc = int(input())
    mv = 0
    col = [0]*100
    left , right =0, 0
    for i in range(100):
        lst = list(map(int,input().split()))
        mv = max(mv, sum(lst))
        for j in range(100):
            col[j] += lst[j]
            if i==j: left += lst[j]
            if i+j==100: right +=lst[j]
    mv=max(mv,left,right)
    for i in range(100):
        mv = max(mv, col[i])
    print("#{} {}".format(tc,mv))
    