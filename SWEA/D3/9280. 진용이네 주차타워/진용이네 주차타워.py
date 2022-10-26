from collections import deque

T = int(input())

def exit(parking, n):
    for i in range(len(parking)):
        if parking[i] == n:
            parking[i] = 0
            return parking

def get_spare(parking):
    for i, v in enumerate(parking):
        if not v:
            return i
    return len(parking)

def ans():
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]
    w = [int(input()) for _ in range(m)]
    sequence = [int(input()) for _ in range(2*m)]
    
    parking = [0] * n
    waiting = deque()
    ans = 0
    for v in sequence:
        if v > 0:
            seat_num = get_spare(parking)
            if seat_num == n:
                waiting.append(v)  
            else:
                ans += r[seat_num] * w[v-1]
                parking[seat_num] = v
        else:
            parking = exit(parking, abs(v))
            seat_num = get_spare(parking)
            if waiting:
                tmp = waiting.popleft()
                parking[seat_num] = tmp
                ans += r[seat_num] * w[tmp-1]
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {ans()}')