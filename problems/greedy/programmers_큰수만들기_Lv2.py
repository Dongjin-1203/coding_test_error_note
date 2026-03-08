"""
[문제] 큰 수 만들기 - 그리디 알고리즘
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42883
[패턴] 그리디 알고리즘
[난이도] Lv.2
[풀이시간] 70분
[재도전여부] Y  # 처음 못 풀었으면 Y

[접근법]
- heapq 기반 다익스트라
- 핵심 인사이트: 방문 처리를 pop 시점에 해야 함

[시간복잡도] O((V + E) log V)
[공간복잡도] O(V + E)

[실수/배운점]
- dist 초기화를 float('inf')로 안 해서 런타임 에러
"""

# ====== 로직 설계 ======
# 1. 큰 수를 찾아서 추가하기 보다 작은 수를 제거하는 방식으로 접근
# 2. 제일 앞자리부터 탐색하며 현재 보다 다음 자리가 더 크면 현재를 제거하고 다음 지리를 현재 자리로 최신화 한다.
# 3. 제거한 수의 개수가 k개가 될 때까지 반복한다.

def solution(number, k):
    answer = []
    for n in number:
        while k > 0:
    return answer

if __name__ == "__main__":
    number_1 = "1924"
    k_1 = 2

    number_2 = "1231234"
    k_2 = 3

    print(solution(number_1, k_1))  
    print(solution(number_2, k_2))