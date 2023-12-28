from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
w, b = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, c):

    q = deque()
    cnt = 0
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if 0 <= x < m and 0 <= y < n and \
            graph[x][y] == c and visited[x][y] == False:
            cnt += 1
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                q.append((nx, ny))

    return cnt


for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            if graph[i][j] == 'W':
                w += bfs(i, j, 'W') ** 2
            else:
                b += bfs(i, j, 'B') ** 2
print(w, b)