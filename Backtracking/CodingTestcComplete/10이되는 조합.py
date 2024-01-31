# 2023.12.26.
# 문제 : 정수 N을 입력받아 1부터 N까지의 숫자 중에서 합이 10이 되는 조합을 리스트로 반환하는 solution() 함수를 작성하세요.
# 제약조건 : 백트래킹 활용 / 오름차순 정렬 / 같은 숫자는 한 번만 선택 / 1=< N =< 10
# 조합한 숫자의 합이 10이 되면 해당 조합을 결과 리스트에 추가하기
# 조합한 숫자의 합이 10보다 크면 백트래킹

def solution(N) :
    results = [] # 조합 결과를 담을 리스트

    def backtrack(sum, selected_nums, start) : 
        if sum == 10: # 합이 10이 되면 결과 리스트에 추가
            results.append(selected_nums)
            return
        
        for i in range(start, N + 1) : # 다음에 선택할 수 있는 숫자들을 하나씩 선택하면서
            if sum + i <= 10: # 선택한 숫자의 합이 10보다 작거나 같으면
                backtrack(
                    sum + i, selected_nums + [i], i + 1) # 백트래킹 함수를 재귀적으로 호출
                
        
    backtrack(0, [], 1) #백트래킹 함수 호출
    return results # 조합 결과 반환
    

