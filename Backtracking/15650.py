from sys import stdin
input = stdin.readline()

N, M = map(int, input.split())
results = []

def backtrack(start):
    if len(results) == M:
        print(" ".join(map(str, results)))
        return

    for i in range(start, N + 1):
        if i not in results:
            results.append(i)
            backtrack(i + 1) # 재귀함수를 호출할때 자신의 다음숫자를 부름
            results.pop()

backtrack(1)