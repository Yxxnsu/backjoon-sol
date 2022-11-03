T = int(input())

def sol():
    
    s = input()

    if s.count('?') == 0:
        if s == s[::-1]:
            return 'Exist'
        else:
            return 'Not exist'
    else:
        if s == s[::-1]:
            return 'Exist'
        else:
            center = len(s) // 2
            front, back = '', ''
            if len(s) % 2 == 0:
                front = s[:center]
                back = s[center:]
                for i in range(len(front)):
                    if front[i] != '?' and back[::-1][i] != '?':
                        if front[i] != back[::-1][i]:
                            return 'Not exist'
                return 'Exist'
            else:
                front = s[:center]
                back = s[center+1:]
                for i in range(len(front)):
                    if front[i] != '?' and back[::-1][i] != '?':
                        if front[i] != back[::-1][i]:
                            return 'Not exist'
                return 'Exist'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')