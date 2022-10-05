from sys import stdin
input = stdin.readline

T = int(input().rstrip())

for _ in range(T):
	N = int(input().rstrip())
	case = list(map(int,input().split()))	
	if len(set(case)) == 1:
		print(0)
	else:
		profit = 0	
		max_value = max(case)
		for i,x in enumerate(case):
			if x != max_value:
				profit += max_value - x
				case[i] = 0
			else:
				case[i] = 0
				max_value = max(case)
		print(profit)
	