from collections import deque


def dfs(visited, v):

	vertax = graph[v]
	visited[v] = True
	print(v, end = ' ')

	for k in vertax:
		if visited[k] == False:
			dfs(visited, k)

def bfs(visited, v):

	visited[v] = True
	
	queue = deque()
	queue.append(v)

	while queue:
		vertax = queue.popleft()
		print(vertax, end = ' ')
		graphs = graph[vertax]
		for k in graphs:
			if visited[k] == False:
				queue.append(k)
				visited[k] = True

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n + 1)

for i in range(m):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	graph[v2].append(v1)
	graph[v1].sort()
	graph[v2].sort()

dfs(visited, v)
visited = [False] * (n+1)
print()
bfs(visited, v)