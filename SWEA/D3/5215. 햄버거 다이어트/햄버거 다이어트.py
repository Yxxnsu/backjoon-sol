T = int(input())

def sol():
    
    N, L = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    def dfs(idx, c_taste, c_kcal):
        global max_tasty
        if c_kcal > L:
            return
        
        if max_tasty < c_taste:
            max_tasty = c_taste
        
        if idx == N:
            return 

        taste, kcal = li[idx]

        dfs(idx + 1, c_taste + taste, c_kcal + kcal)
        dfs(idx + 1, c_taste, c_kcal)
    
    dfs(0, 0, 0)

    return max_tasty

for tc in range(1, T+1):
    max_tasty = 0
    print(f'#{tc} {sol()}')