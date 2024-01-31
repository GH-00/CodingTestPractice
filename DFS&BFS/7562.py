# 2024.01.05.
from collections import deque
import sys

input = sys.stdin.readline

# 테스트 케이스의 개수를 입력받음
t = int(input().rstrip())

# BFS 함수 정의
def bfs():
    # 기체 나이트의 8가지 이동 방향
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    # BFS를 위한 큐 초기화
    q = deque()
    q.append((startX, startY))

    # 이동 횟수를 기록하는 2차원 배열 초기화
    matrix = [[0] * n for _ in range(n)]
    matrix[startX][startY] = 1

    # BFS 탐색 시작
    while q:
        x, y = q.popleft()

        # 목표 위치에 도달하면 최소 이동 횟수를 반환
        if x == endX and y == endY:
            return matrix[x][y] - 1 # 처음에 시작 위치의 이동 횟수를 1로 초기화 해서 1을 빼줘야함

        # 8가지 방향으로의 이동을 검사
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 유효한 범위 내에 있고, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
                # 이동 횟수를 업데이트하고 큐에 새로운 위치를 추가
                # 현재까지 이동 횟수에 1을 더한 값으로 갱신. 새로운 위치로 이동 하는데 필요한 최소 이동 횟수
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))

# 각 테스트 케이스에 대해 반복
for _ in range(t):
    # 체스판의 크기와 시작, 목표 위치 입력
    n = int(input().rstrip())
    startX, startY = map(int, input().rstrip().split())
    endX, endY = map(int, input().rstrip().split())

    # BFS 호출하여 결과 출력
    result = bfs(startX, startY, endX, endY, n)
    print(result)
