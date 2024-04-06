import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split()) #정점 수, 간선 수, 시작 정점

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

# M개의 연결된 간선 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순으로 인접노드 방문하기 위해 정렬
for i in range(N + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt #방문하면 순서 나타내기

    for i in graph[v]:
        if not visited[i] :
            cnt += 1
            dfs(graph, i, visited)

dfs(graph, R, visited)

for i in range(1, N + 1):
    print(visited[i])

