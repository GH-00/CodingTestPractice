import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = {}

# n개의 단어를 입력받아서 처리
for _ in range(n):
    name = input().strip()  # 입력받은 단어, 양쪽 공백 제거

    # 단어의 길이가 m보다 작으면 패스
    if len(name) < m:
        continue

    # 딕셔너리 d에 단어를 키로 저장
    if d.get(name):
        # 이미 존재하는 단어일 경우 개수 증가
        d[name][0] += 1
    else:
        # 새로운 단어일 경우 [개수, 길이, 단어] 정보를 저장
        d[name] = [1, len(name), name]

# 정렬 기준에 따라 정렬
# 1. 개수를 기준으로 내림차순 정렬 (-x[1][0])
# 2. 개수가 같으면 길이를 기준으로 내림차순 정렬 (-x[1][1])
# 3. 길이도 같으면 단어를 기준으로 사전순(오름차순) 정렬 (x[1][2])
ans = sorted(d.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

# 정렬된 결과를 출력
for a in ans:
    print(a[0])  # 단어만 출력
