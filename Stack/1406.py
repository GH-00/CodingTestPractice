# retry! handwriting 해보기!
import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
M = int(input().rstrip())

left = deque([i for i in s])
right = deque()
for _ in range(M):
    temp = list(map(str,input().rstrip().split()))

    if temp[0] == 'P':
        left.append(temp[1])

    if temp[0] == 'L':
        if left: # 커서가 맨 앞이 아닌 경우에는
            word = left.pop()
            right.appendleft(word)

    if temp[0] == 'D':
        if right: # 커서가 맨 뒤가 아닌 경우에는
            word = right.popleft()
            left.append(word)

    if temp[0] == 'B':
        if left: # 커서가 맨 앞이 아닌 경우에는
            left.pop()

left = list(left)
right = list(right)
print(''.join(map(str,left+right)))
