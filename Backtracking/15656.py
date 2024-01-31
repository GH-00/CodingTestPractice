#2023.12.30.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def backtrack():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    # for i in range(N) 은 가능
    # for i in range(1, N + 1)은 불가능 -> 인덱스 범위 설정이 잘못됨
    for i in range(0, N):
        res.append(arr[i])
        backtrack()
        res.pop()

backtrack()
