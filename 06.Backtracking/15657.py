#2023.12.30.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def backtrack(start):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    for i in range(start, N):
        res.append(arr[i])
        backtrack(i)
        res.pop()

backtrack(0)
