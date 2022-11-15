T = 10

def sol():

    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    
    ans = 0
    for i in range(8):
        for j in range(8-N+1):
            if matrix[i][j:j+N] == matrix[i][j:j+N][::-1]:
                ans += 1
    
    def rotate_matrix_90_degree(m):

        n_matrix = [[''] * 8 for _ in range(8)]

        for i in range(8):
            for j in range(8):
                n_matrix[j][7-i] = m[i][j]
        return n_matrix

    matrix = rotate_matrix_90_degree(matrix)

    for i in range(8):
        for j in range(8-N+1):
            if matrix[i][j:j+N] == matrix[i][j:j+N][::-1]:
                ans += 1

    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')