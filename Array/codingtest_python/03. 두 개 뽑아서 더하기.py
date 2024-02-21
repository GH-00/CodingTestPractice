# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환

# 배열에서 두 수를 선택하는 방법 -> 자신보다 뒤에 있는 수를 선택하면 됨!
def solution(numbers):
    ret = [] # 빈 배열 생성
    # 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for i in range (len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers(j))
    # 중복된 값을 제거하고, 오름차순으로 정렬
    ret = sorted(set(ret))
    return ret # 최종 결과 반환