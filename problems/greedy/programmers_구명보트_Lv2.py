"""
[문제] 구명보트 - 그리디 알고리즘
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42885
[패턴] 그리디 알고리즘
[난이도] Lv.2
[풀이시간] 60분
[재도전여부] Y  # 처음 못 풀었으면 Y

[접근법]
- 몸무게 리스트(people)를 오름차순 정렬
- 가장 무거운 사람과 가장 가벼운 사람을 pairing하여 구명보트를 사용

[시간복잡도] O((V + E) log V)
[공간복잡도] O(V + E)

[실수/배운점]
- dist 초기화를 float('inf')로 안 해서 런타임 에러
"""

# ====== 로직 설계 ======
# 1. people 리스트를 오름차순으로 정렬
# 2. 투 포인터를 사용하여 가장 무거운 사람과 가장 가벼운 사람을 pairing
# 3. 무거운 사람을 태우고 가벼운 사람들을 탐색하며 limit을 초과하지 않는 범위 내에서 태움
# 4. 태울 사람이 추가로 없다면 무거운 사람만 태우고 다음으로 넘어감

def solution(people, limit):
    answer = 0

    people.sort()
    left, right = 0, len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer

if __name__ == "__main__":
    people_1 = [70, 50, 80, 50]
    limit_1 = 100

    people_2 = [70, 80, 50]
    limit_2 = 100

    print(solution(people_1, limit_1))  
    print(solution(people_2, limit_2))  