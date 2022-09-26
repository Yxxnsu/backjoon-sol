s = input()

if len(set(s)) == 1:
	print(0)

else:

	element = ["0","1"]
	result = []

	for e in element:
		continous = cnt = 0
		for i in range(len(s)):
			if i == len(s) - 1 and s[i] == e:
				cnt += 1
			if s[i] == e:
				continous += 1
			else:
				if continous > 0:
					cnt += 1
					continous = 0
		result.append(cnt)
	print(min(result))