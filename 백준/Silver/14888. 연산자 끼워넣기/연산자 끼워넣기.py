from itertools import permutations

times = int(input())
numbers = [int(x) for x in input().split()]
add, sub, mul, div = map(int, input().split())

# get operator list
operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div

oprt_prmt = list(set(permutations(operators, len(operators))))
min_value, max_value = 1e9, -1e9

for i in range(len(oprt_prmt)):
	
    temp = numbers[0]
    
    for j in range(len(oprt_prmt[i])):
        if oprt_prmt[i][j] == '+':
            temp += numbers[j + 1]
        elif oprt_prmt[i][j] == '-':
            temp -= numbers[j + 1]
        elif oprt_prmt[i][j] == '*':
            temp *= numbers[j + 1]
        else:
            if temp < 0:
                temp = abs(temp) // numbers[j + 1]
                temp = temp * (-1)
            else:
                temp //= numbers[j + 1]
                
    if min_value > temp:
        min_value = temp
    if max_value < temp:
        max_value = temp
	
print(f'{max_value}\n{min_value}')