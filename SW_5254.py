def calc_lcp(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    ret = 0
    for i in range(min(len_s1,len_s2)):
        if s1[i] != s2[i]: break
        ret += 1
    return ret
def part_string(suffix, N , S_len):
    LCP = 0
    for i in range(S_len -1):
        curr_idx , curr_string = suffix[i]
        if len(curr_string) - LCP >= N:
            return curr_string[:N+LCP]
        else:
            N -= (len(curr_string) - LCP)
            LCP = calc_lcp(curr_string, suffix[i+1][1])
    return ""

T = int(input())
for case in range(1,T+1):
    print("#{} ".format(case), end="")
    N , S = input().split()
    S_len ,suffix = len(S), []
    for i in range(S_len):
        suffix.append((i,S[i:]))
    suffix.sort(key = lambda elements : elements[1])
    partition_string = part_string(suffix,int(N),S_len)
    print(partition_string[0] , len(partition_string))

