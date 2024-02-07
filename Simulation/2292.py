import sys
input = sys.stdin.readline

n = int(input())
hives = 1
for i in range(n):
    hives += i*6  # i 번째 겹인 벌집 개수는 6의 배수로 늘어남
    if n <= hives: # 벌집 개수의 누적이 입력값보다 커지면
        print(i+1) #(i+1)번 째 겹인 것이므로 출력
        break