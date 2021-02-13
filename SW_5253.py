T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end ="")
    N, M =map(int,input().split())
    A_prefix_array = set()
    for i in range(N):
        A = input()
        new_string = ''
        for x in A:
            new_string += x
            A_prefix_array.add(new_string)
    result = 0
    for i in  range(M):
        B = input()
        if B in A_prefix_array: result +=1
    print(result)