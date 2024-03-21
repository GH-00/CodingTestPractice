# A의 성적이 B의 성적보다 둘 다 안좋으면 A는 선발 안됨 -> 최대 인원수
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort() # 앞에있는 서류 기준으로 정렬하자! 서류 1위는 무조건 합격
    check = arr[0][1] # 서류 1등의 면접 기준로 순위 비교!

    people = 1  #서류 1등은 무조건 합격

    for i in range(1, N):
        if arr[i][1] < check:
            people +=1
            check = arr[i][1]
    print(people)




