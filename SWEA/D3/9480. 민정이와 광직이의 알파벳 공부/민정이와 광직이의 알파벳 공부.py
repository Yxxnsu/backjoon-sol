from itertools import combinations

T = int(input())
 
def sol():

    N = int(input())
    li = [input() for _ in range(N)]
    comb_li = []

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(1, N+1):
        arr = list(combinations(li,i))
        for j in range(len(arr)):
            comb_li.append(''.join(arr[j]))

    ans = 0
    for v in comb_li:
        cnt = 0
        for s in alpha:
            if s in v:
                cnt += 1
        if cnt == 26:
            ans += 1
    
    return ans
        
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')