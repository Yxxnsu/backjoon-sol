def get_max_value(N):
	new_N = N.copy()
	asc_N = sorted(N, reverse = True)
	k = 0
	for i, v in enumerate(new_N):
		if v == asc_N[k]:
			k += 1
			continue
		else:
			s = ''.join(N)
			idx = s.rindex(asc_N[k])			
			new_N[i], new_N[idx] = new_N[idx], new_N[i]
			break
	return new_N

def get_min_value(N):
	
	new_N = N.copy()
	
	desc_N = sorted(N)
	desc_N_not_zero = [x for x in desc_N if x != '0']
	
	k = 0
	if N[0] == desc_N_not_zero[0]:
		tmp = N[1:]
		desc_N.remove(N[0])

		for i, v in enumerate(tmp):
			if v == desc_N[k]:
				k += 1
				continue
			else:
				s = ''.join(tmp)
				idx = s.rindex(desc_N[k])
				tmp[i], tmp[idx] = tmp[idx], tmp[i]
				tmp.insert(0,N[0])
				return tmp
	else:
		s = ''.join(N)
		idx = s.rindex(desc_N_not_zero[0])
		new_N[0], new_N[idx] = new_N[idx], new_N[0]
		return new_N
	return N	

T = int(input())

for idx in range(1, T+1):
	
	N = list(input())

	if set(N) == {'0'}:
		temp = ''.join(N)
		print(f'#{idx} {temp} {temp}')
	else:	
		min_value = ''.join(get_min_value(N))
		max_value = ''.join(get_max_value(N))
		print(f'#{idx} {min_value} {max_value}')