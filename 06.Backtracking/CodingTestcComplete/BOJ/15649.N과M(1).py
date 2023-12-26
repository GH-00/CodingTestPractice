import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
results = []

def backtrack() :
    if len(results) == M :
        print(" ".join(map(str, results)))
        return

    for i in range (1, N + 1):
        if i not in results :
            results.append(i)
            backtrack()
            results.pop()

backtrack()