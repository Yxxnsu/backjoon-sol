i = 0
result = []
while i < 100:
	try:
		result += [input()]
		i += 1
	except EOFError:
		break
for x in result:
	print(x)
		