import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = []

def backtrack(depth):
    if depth == M:
        print(' '.join(map(str, visited)))
        return

    for i in range(N):
        if nums[i] in visited:
            continue
        visited.append(nums[i])
        backtrack(depth + 1)
        visited.pop()

backtrack(0)
