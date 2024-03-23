# 스위치 개수
switch_count = int(input())
# 각 스위치의 상태 (1 켜져있음 0 꺼져있음)
switch_state = list(map(int, input().split()))
switch_state.insert(0, 0) # 인덱스 이동
# 학생 수   
student_count = int(input())
# 학생의 성별, 학생이 받은 수
student_switch = [list(map(int, input().split())) for _ in range(student_count)]

for gender, number in student_switch:

    if gender == 1:  # 남학생
        number_up = number
        while number_up < len(switch_state):
            switch_state[number_up] = 1 if switch_state[number_up] == 0 else 0
            number_up += number

    else:  # 여학생
        switch_state[number] = 1 if switch_state[number] == 0 else 0
        left = number - 1
        right = number + 1
        while left > 0 and right < switch_count + 1 and switch_state[left] == switch_state[right]:
            switch_state[left] = 1 if switch_state[left] == 0 else 0
            switch_state[right] = 1 if switch_state[right] == 0 else 0
            left -= 1
            right += 1

for num in range(1, len(switch_state)):
    print(switch_state[num], end=" ")
    if num % 20 == 0: print() # 한 줄에 20개씩 출력