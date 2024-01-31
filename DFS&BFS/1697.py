import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
cut = abs(b - a)
visited = [False for i in range(200001)]
q = deque()
visited[b] = True
q.append((b, 0))

while True:
    x, c = q.popleft()
    if x == a:
        print(c)
        break
    if c >= cut:
        print(cut)
        break
    if x % 2 == 0 and visited[x//2] == False:
        visited[x // 2] = True
        q.append((x // 2, c + 1))
    if visited[x - 1] == False:
        visited[x - 1] = True
        q.append((x - 1, c + 1))
    if visited[x + 1] == False:
        visited[x + 1] = True
        q.append((x + 1, c + 1))


