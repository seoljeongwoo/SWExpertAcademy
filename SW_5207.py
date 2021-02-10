def B_search(low, high, target):
    mid = (low+high)//2
    prev = ''
    if A[mid] == target: return True
    elif A[mid] > target:
        prev = 'L'
        high = mid-1
    else:
        prev = 'R'
        low = mid+1
    
    while low<=high:
        mid = (low+high)//2
        _next =''
        if A[mid] == target:
            return True
        elif A[mid] > target:
            _next = 'L'
            high = mid-1
        else:
            _next = 'R'
            low = mid+1

        if prev == _next: return False
        else: prev = _next
    return False
        

T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N,M=map(int,input().split())
    A,B=list(map(int,input().split())), list(map(int,input().split()))
    A.sort()
    C = 0 
    for data in B:
        mid = N//2
        if B_search(0,N-1,data):
            C+=1
    print(C)