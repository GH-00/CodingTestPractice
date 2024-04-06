import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = [0] * (N + 1)
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    global cnt
    visited[v] = True

    ans[v] = cnt

    graph[v].sort(reverse=True)

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(R)

for i in ans[1:]:
    print(i)
