T = int(input())

def sol():

    word = list(input())

    H = int(input())
    li = list(map(int, input().split()))
    li.sort(reverse=True)

    for v in li:
        word.insert(v, '-')
    
    return ''.join(word)
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')