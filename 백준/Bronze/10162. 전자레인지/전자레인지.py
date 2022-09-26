cook = int(input())

button = [300, 60, 10]

a = cook // 300
b = cook % 300 // 60
c = cook % 300 % 60 // 10

cook = cook % 300 % 60 % 10

print(a,b,c) if cook == 0 else print(-1)
	
	
