from collections import deque

n = int(input()) # 정점 개수
e= int(input()) # 간선 개수
count = 0

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue= deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)

bfs(graph,1, visited)
print(sum(visited) - 1)