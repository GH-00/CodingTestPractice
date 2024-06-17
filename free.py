from collections import deque

X = int(input())
def solution(X):
    queue = deque([(X, 0)])  # 시작 노드와 연산 횟수를 큐에 저장
    visited = set()  # 방문한 노드를 저장하는 집합
    visited.add(X)  # 시작 노드 방문 표시

    while queue:
        number, count = queue.popleft()  # 큐에서 노드와 연산 횟수 가져오기

        # 1에 도달한 경우, 연산 횟수 반환
        if number == 1:
            return count

        # 4가지 연산을 수행하고, 방문하지 않은 노드라면 큐에 추가
        for next_number in [number // 5 if number % 5 == 0 else number,
                            number // 3 if number % 3 == 0 else number,
                            number // 2 if number % 2 == 0 else number,
                            number - 1]:
            if next_number not in visited:
                visited.add(next_number)
                queue.append((next_number, count + 1))

    return -1  # 1에 도달하지 못한 경우

print(solution(X))