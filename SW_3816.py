T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case),end="")
    S1,S2 = input().split()
    S1_Count , S2_Count = [0] * 26 , [0] * 26
    for x in S1:
        S1_Count[ord(x) - ord('a')] += 1
    for loop in range(len(S1)):
        S2_Count[ord(S2[loop]) - ord('a')] +=1
    i ,j,ret =0,len(S1)-1,0
    while j<len(S2):
        ok = True
        for loop in range(26):
            if S1_Count[loop] > S2_Count[loop]:
                ok = False
                break
        if ok: ret+=1
        
        S2_Count[ord(S2[i]) - ord('a')] -=1
        i+=1; j+=1
        if j!= len(S2): S2_Count[ord(S2[j]) - ord('a')] +=1
    print(ret)
        