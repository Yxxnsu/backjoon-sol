T = int(input())

def sol():

    matrix = [list(input()) for _ in range(5)]

    max_length = max([len(l) for l in matrix])
    
    ans = []
    for i in range(max_length):
        for j in range(5):
            try:
                ans.append(matrix[j][i])
            except IndexError:
                continue
    return ''.join(ans)
 
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')