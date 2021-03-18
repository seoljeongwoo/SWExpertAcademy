for _ in range(10):
    testcase = int(input())
    search , st = input() , input()
    idx ,cnt = -1 , 0
    while True:
        idx = st.find(search,idx+1)
        if idx == -1: break
        cnt+=1
    print("#{} {}".format(testcase,cnt))