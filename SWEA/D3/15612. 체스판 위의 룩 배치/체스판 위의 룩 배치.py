from collections import deque
 
T = int(input())
 
def sol():

    chess = [list(input()) for _ in range(8)]
    
    cnt = 0
    for i in range(8):
        if chess[i].count('O') != 1:            
            return 'no'
        cnt += chess[i].count('O') 
        c_cnt = 0
        for j in range(8):
            if chess[j][i] == 'O':
                c_cnt += 1
        if c_cnt != 1:
            return 'no'
    if cnt != 8:
        return 'no'
    return 'yes'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')