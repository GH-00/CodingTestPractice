# 배열의 중복값을 제거하고 배열 데이터를 내림차순으로 정렬해서 반환하기

def solution(list):
    unique_list = list(set(list)) # 중복값 제거하기
    unique_list.sort(reverse=True) #내림차순 정렬
    return unique_list