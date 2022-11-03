T = int(input())

def sol():

    s = input()

    li = [list() for _ in range(4)]

    data = {'S':0,'D':1,'H':2,'C':3}

    for i in range(0, len(s), 3):
        c = s[i]
        num = int(s[i+1] + s[i+2])  
        idx = data[c]    
        
        if num in li[idx]:
            return 'ERROR'
        li[idx].append(num)

    ans = []
    for v in li:
        ans.append(f'{13 - len(v)}')
    return ' '.join(ans)
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')