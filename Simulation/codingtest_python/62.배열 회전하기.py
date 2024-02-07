# 2차원 배열 arr을 시계 방향으로 90도 *n번 회전하는  solution() 함수 작성
# 일반화 식 : A[i, j] = A[j, (N - 1) - i]

def solution(arr, n):
    # 2차원 배열을 인자로 받고, 90도 회전시키는 함수
    def rotation_90(arr):
        # 배열의 크기 저장
        n = len(arr)
        
        # 배열의 크기와 동일한 2차원 배열 생성(초기값은 0)
        rotated_arr = [[0] * n for _ in range(n)]

        # 배열을 90도 회전
        for i in range(n):
            for j in range(n):
                rotated_arr[j][n - i - 1] = arr[i][j]

        # 90도로 회전한 배열 반환
        return rotated_arr

    # 원본배열 arr을 복사
    rotated_arr = arr.copy()

    # 90도 회전 함수 호출
    for _ in range(n):
        rotated_arr = rotation_90(rotated_arr)

    return rotated_arr
