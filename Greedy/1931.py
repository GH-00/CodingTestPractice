import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s,e))

arr.sort(key = lambda x : (x[1], x[0]))

curr = arr[0][1] # 가장 빠른 회의 시간의 두번째 인덱스(종료시간) -> 현재 회의 종료시간
room = 1 # 현재 회의실은 먼저 할당!

# 회의시간의 시작 시간이 현재 종료시간보다 커야함
for i in range(1, N):
    if arr[i][0] >=curr:
        curr= arr[i][1] # 다음 회의종료 시간을 현재회의로 갱신!!!!!
        room +=1

print(room)
