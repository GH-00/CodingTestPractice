# 2024. 01. 07.
from collections import deque
import sys
input = sys.stdin.readline

# bfs 특 queue 사용하기
# deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)

M, N = map(int, input().split())
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [list(map(int, input().split())) for _ in range(N)]

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# n과 m을 사용하는걸 헷갈리지 말아야 함!
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

# 정답이 담길 변수
res = 0

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while q:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = q.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny]==0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
bfs()

for line in graph:
    for tomato in line:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if tomato == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(line))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)



