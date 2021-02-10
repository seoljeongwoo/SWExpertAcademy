T = int(input())
for _ in range(T):
    print("#{} ".format(_+1),end="")
    N ,lst = int(input()), list(map(int,input().split()))
    def quick(start, end):
        global lst
        if end-start <= 1: return
        pivot = lst[(start+end)//2]
        left , right = start, end
        while left <= right:
            while lst[left] < pivot: left+=1
            while  lst[right] > pivot : right-=1

            if left<=right:
                lst[left], lst[right] = lst[right], lst[left]
                left+=1; right-=1
        quick(start, right)
        quick(left,end)
        return
    quick(0,N-1)
    print(lst[N//2])
    