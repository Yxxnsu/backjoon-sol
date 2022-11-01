import sys
sys.setrecursionlimit(10**5)

T = int(input())

def sol():

    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    def dfs(x, y):
        
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        else:
            if matrix[x][y] == 1:
                matrix[x][y] = 0
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)            
                return True        
            return False
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                ans += 1
    return ans

for tc in range(T):
    print(f'{sol()}')