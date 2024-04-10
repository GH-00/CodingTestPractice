from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001  #최대 0부터 100000까지의 지점까지 걸리는 횟수 기록

# BFS 탐색
queue = deque()
queue.append(N)  # 시작점

cnt = 0  # 최적경로 수
min_path = 0  # 최소 시간

# 큐가 빌 때까지 탐색
while queue:
    x = queue.popleft()
    # 도착지점이라면 탐색 종료
    if x == K:
        min_path = visited[x]
        cnt += 1
        continue

    # x에서 -1 또는 +1 또는 *2 탐색
    for nextX in (x+1, x-1, 2*x):
        # 0~100000지점 내이고, 방문하지 않았거나 동일한 탐색횟수를 가졌으면 탐색
        if 0 <= nextX <= 100000 and (visited[nextX] == 0 or visited[nextX] == visited[x]+1):
            visited[nextX] = visited[x] + 1  # 방문하고 횟수 1늘림
            queue.append(nextX)  # 큐에 추가

# 출력
print(min_path)
print(cnt)