import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
arr = []

def backtrack():
    if len(arr) == M :
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr.append(i)
        backtrack()
        arr.pop()

backtrack()