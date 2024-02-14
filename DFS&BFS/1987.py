# 최장거리 출력
# DFS / BFS
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(g):
    result = 1
    q = set()
    # 현재 위치 x, y 지금까지 지나온 알파벳 문자열로 저장
    q.add((0, 0, graph[0][0]))

    while q and result != 26:
        x, y, road = q.pop()
        result = max(result, len(road))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] not in road:
                q.add((nx, ny, road + g[nx][ny]))
    print(result)


bfs(graph)