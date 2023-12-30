# 2023.12.30.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

def backtrack(start):
    if len(arr) == M :
        print(" ".join(map(str, arr)))
        return

    for i in range(start, N + 1):
        arr.append(i)
        backtrack(i)
        arr.pop()

backtrack(1)
