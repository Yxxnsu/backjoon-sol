from itertools import combinations

T = int(input())

def sol():
    
    nl = list(map(int, input().split()))
    ans = []

    for v in list(combinations(nl, 3)):
        ans.append(sum(v))
    ans = list(set(ans))   
    ans.sort(reverse=True)
    return ans[4]

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')