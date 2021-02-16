from math import exp
import random
Case = int(input())
for _ in range(1,Case+1):
    print("#{} ".format(_),end="")
    T,T_end,k = map(float,input().split())
    cost_prev = float('inf')
    count = 0
    while T>T_end:
        count += 1
        cost_new = 123456789
        diff = cost_new - cost_prev 
        if diff < 0 or exp(-diff/T) > random.random():
            cost_prev = cost_new
        T = T*k
    print(count)

