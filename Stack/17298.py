import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

NGE = [-1] * N
stack = [] # 인덱스를 저장할 스택

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i) # 인덱스 업데이트

print(*NGE)