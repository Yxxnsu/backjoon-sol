T = int(input())
dd = {'MON':1,'TUE':2,'WED':3,'THU':4,'FRI':5,'SAT':6,'SUN':7}

for idx in range(1, T+1):
	day = input() 
	num_of_day = dd[day]
	if 7 - num_of_day == 0:
		print(f'#{idx} 7')
	else:
		print(f'#{idx} {7-num_of_day}')