# bfs
# python3로 했을 때는 시간 초과 =>  input() 을 sys.stdin.readline() 으로 치환!!
# 유니온 파인드로 다시 풀어보기!

from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
count = 0

graph= [[] for _ in range(n+1)]
for _ in range(m):
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

result = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        result +=1

print(result)