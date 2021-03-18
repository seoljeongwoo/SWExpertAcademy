tc = int(input())
for _ in range(1,tc+1):
    n,m,k = map(int,input().split())
    customer = list(map(int,input().split()))
    customer.sort()
    bread = 0
    time , j = 0, 0
    ok =True
    while j<len(customer):
        if time>0: bread += k
        cnt = 0 
        while j<len(customer) and customer[j] <time+m: cnt+=1 ; j+=1
        bread -= cnt
        if bread<0: ok=False;break
        time+=m
    
    if ok: print("#{} Possible".format(_))
    else: print("#{} Impossible".format(_))

    
