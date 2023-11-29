import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().rstrip()))
    graph.append(a)


def bfs(x, y):
    # 상,하,좌,우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))  # 튜플

    while True:
        if len(q) == 0:
            break
        x, y = q.popleft()  # 리스트, 튜플 모두 이 방법 사용 가능하다.

        # 상,하,좌,우 인접한 값들 중 가능한 것들의 최소 시간 업데이트
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어난 값이면 탐색하지 않는다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 아직 최소시간이 정해지지 않은 곳만 + 벽이 아닌 곳
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))  # 업데이트 해줬으면 큐에 넣어서 업데이트 해준 값의 인접 값도 업데이트 해줘야 함.

    # 모든 1에 대해 업데이트가 끝났다면 큐가 텅 비게 되고, while 반복문이 종료되어 아래로 내려온다.
    return graph[n - 1][m - 1]


print(bfs(0, 0))
