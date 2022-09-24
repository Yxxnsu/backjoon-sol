s = input()

if len(s) == 0:
	print(0)
else:
	stack = []
	start = end = 0
	for i in range(len(s)):
		
		if i == len(s) - 1:
			end = len(s)
			stack.append(int(s[start:end]))
			
		if s[i] == "+" or s[i] == "-":
			end = i
			stack.append(int(s[start:end]))
			stack.append(s[i])
			start = i + 1			
		else:
			continue

	stack = list(map(str, stack))
	minus_divid = "".join(stack).split("-")


	# if "-" not in minus_divid:
	# 	print(eval(minus_divid))
	# else:
	# 	sum = eval(minus_divid[0])
	
	sum = eval(minus_divid[0])
	
	for i in range(1, len(minus_divid)):
		if "+" in minus_divid[i]:
			sum -= eval(minus_divid[i])
		else:
			sum -= int(minus_divid[i])
	
	print(sum)
	
	
		
		
