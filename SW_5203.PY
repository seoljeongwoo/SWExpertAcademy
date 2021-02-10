def check(arr , value):
    if arr[value] ==3: return True
    for i in range(value-2,value+1):
        if i<0 or i+2>=10: continue
        if arr[i] > 0 and arr[i+1] >0 and arr[i+2]>0:
            return True
    return False

T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    lst = list(map(int,input().split()))
    A,B=[0]*10,[0]*10
    winner = 0
    for i in range(len(lst)):
        if i%2 == 0:    # turn 1
            A[lst[i]]+=1
            if check(A,lst[i]) == True: 
                winner = 1
                break
        else:           # turn 2
            B[lst[i]]+=1
            if check(B,lst[i]) == True:
                winner = 2
                break
    print(winner)

