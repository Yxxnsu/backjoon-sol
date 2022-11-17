T = 10

def sol():

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
       
    def rotate_matrix_by_90_degree(matrix):
        n_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                n_matrix[j][N-1-i] = matrix[i][j]
        return n_matrix

    matrix = rotate_matrix_by_90_degree(matrix)

    ans = 0
    for v in matrix:
        s = ''.join([str(x) for x in v if x != 0])
        ans += s.count('21')
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')