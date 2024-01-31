# 2024.01.01.
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))

res = []
visited = [0 for _ in range(N)]

def backtrack():
    if len(res) == M:
        print(*res)
        return

    ex = 0
    for i in range(len(arr)):
        if ex != arr[i] and visited[i] == 0:
            res.append(arr[i])
            visited[i] = 1
            backtrack()
            ex = res.pop()
            visited[i] = 0


backtrack()

