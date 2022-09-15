number, m = map(int, input().split())
l = [int(x) for x in input().split()]
near = 0
for i in range(number):
	if near == m:
		break
	for j in range(i+1, number):
		if near == m:
			break
		for k in range(j+1, number):
			if l[i] + l[j] + l[k] == m:
				near = m
				break
			elif l[i] + l[j] + l[k] < m:
				if l[i] + l[j] + l[k] > near:
					near = l[i] + l[j] + l[k]
			else:
				continue
				
print(near)	

	
