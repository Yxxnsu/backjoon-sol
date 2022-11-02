import sys
sys.setrecursionlimit(10 ** 5)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    
    matrix = [list(map(int, input().split())) for _ in range(h)]


    def dfs(x, y):
        
        if matrix[x][y] == 1:
            
            matrix[x][y] = 0        
            
            for i in range(8):
                
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue

                if matrix[nx][ny] == 1:
                    dfs(nx, ny)
                
            return True 
        
        return False

    ans = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                ans += 1
    print(ans)