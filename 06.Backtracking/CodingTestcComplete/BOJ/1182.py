# 2023.12.28.
from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
arr = []
cnt = 0

def backtrack(start):
    global cnt
    if len(arr) > 0 and sum(arr) == S:
        cnt += 1

    for i in range(start, N):
        arr.append(num[i])
        backtrack(i+1)
        arr.pop()

backtrack(0)
print(cnt)