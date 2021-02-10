T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N ,lst = int(input()), list(map(int,input().split()))
    C = 0
    def partition(arr):
        global C
        if len(arr) <=1: return arr
        mid = len(arr)//2
        left = partition(arr[:mid])
        right = partition(arr[mid:])
        if(max(left) > max(right)): C+=1
        return arr
    partition(lst)
    lst.sort()
    print(lst[N//2] , C)