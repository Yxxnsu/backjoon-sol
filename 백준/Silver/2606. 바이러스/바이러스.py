def dfs(visited, v):
	global worm
	visited[v] = True

	for vertax in graph[v]:
		if visited[vertax] == False:
			worm += 1
			dfs(visited, vertax)
	
v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
worm = 0

for _ in range(e):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	graph[v2].append(v1)

dfs(visited, 1)
print(worm)