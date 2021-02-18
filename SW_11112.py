T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")
    p,q,r=map(int,input().split())
    a,b,c,d =map(int,input().split())

    if a<=p-r and p+r<=c and b<= q-r and q+r<=d: print("N" ,end="")
    else :print("Y",end="")
    
    if (p-a)**2+(q-b)**2 <= r**2 and (p-a)**2+(q-d)**2 <=r**2 and (p-c)**2+(q-b)**2 <=r**2 and (p-c)**2+(q-d)**2 <= r**2: print("N")
    else: print("Y")