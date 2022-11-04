T = int(input())

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,1,-1]

def sol():

    N, M = map(int, input().split())

    def BWCount(matrix):        
        res = [0,0]
        for v in matrix:
            res[0] += v.count(1)
            res[1] += v.count(2)
        res = map(str, res)
        return res

    def isWhat(nx, ny, color, matrix):

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return 0
        elif matrix[nx][ny] == 0:
            return 0
        elif matrix[nx][ny] != color:
            return 1
        else:
            return 2

    def paint(x, y, color, matrix):
        
        matrix[x][y] = color

        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            store = []

            while True:
                
                maker = isWhat(nx, ny, color, matrix)

                if maker == 0:
                    break

                elif maker == 1:
                    store.append([nx,ny])

                elif maker == 2:
                    for v in store:
                        x1, y1 = v
                        matrix[x1][y1] = color
                    break
                
                nx += dx[i]
                ny += dy[i]                

    def makeMatrix():
        matrix = [[0] * N for _ in range(N)]
        
        k = N // 2
        matrix[k-1][k-1] = 2
        matrix[k][k] = 2
        matrix[k][k-1] = 1
        matrix[k-1][k] = 1

        return matrix

    matrix = makeMatrix()

    ans = []
    for _ in range(M):
        x, y, color = map(int, input().split())
        
        paint(y-1, x-1, color, matrix)

    ans = BWCount(matrix)

    return ' '.join(ans)

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')