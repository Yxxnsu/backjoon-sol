num = int(input())
total, creator = 0, 0
for i in range(1, num + 1):
	s = [int(x) for x in str(i)]
	total = sum(s) + i
	if total == num:
		creator = i
		break
	else:
		continue
print(creator)