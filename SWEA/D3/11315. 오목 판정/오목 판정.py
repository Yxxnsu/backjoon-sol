T = int(input())

def sol():

    N = int(input())

    matrix = [list(input()) for _ in range(N)]

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    cnt = 1
                    while 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 'o':
                        nx += dx[k]
                        ny += dy[k]
                        cnt += 1
                        if cnt == 5:
                            return 'YES'
    return 'NO'                            

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')