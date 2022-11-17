from collections import deque

T = 10

def sol():

    tc = int(input())
    li = deque(list(map(int, input().split())))

    i = 1
    while li:
        if i > 5: i = 1
        front = li.popleft()
        if front - i <= 0:
            li.append(0)        
            break
        else:
            li.append(front-i)
        i += 1
    return ' '.join(map(str,li))

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')