T = int(input())

for idx in range(1,T+1):
	N = int(input())
	case = list(map(int,input().split()))	
	profit = 0
	if len(set(case)) == 1:
		print(f'#{idx} {0}')
	else:
		while case:
			max_value = max(case)
			max_idx = case.index(max_value)
			for i in range(max_idx):
				profit += max_value - case[i]
			case = case[max_idx + 1:]
		print(f'#{idx} {profit}')		