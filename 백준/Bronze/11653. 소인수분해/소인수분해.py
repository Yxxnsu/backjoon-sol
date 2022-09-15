num = int(input())
i = 2
while num != 1:
	if num % i != 0:
		i += 1
	else:
		num //= i
		print(i)