T = 10
N = 100

def sol():

    tc = int(input())
    matrix = [list(input()) for _ in range(N)]
    
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(j+1,N+1):
                l = len(matrix[i][j:k])
                if ans >= l:
                    continue
                else:
                    if matrix[i][j:k] == matrix[i][j:k][::-1]:
                        ans = l
    
    def rotate_matrix_90_by_degree(m):

        n_matrix = [[''] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                n_matrix[j][N-1-i] = m[i][j]
        return n_matrix

    matrix = rotate_matrix_90_by_degree(matrix)

    for i in range(N):
        for j in range(N):
            for k in range(j+1,N+1):
                l = len(matrix[i][j:k])
                if ans >= l:
                    continue
                else:
                    if matrix[i][j:k] == matrix[i][j:k][::-1]:
                        ans = l
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')