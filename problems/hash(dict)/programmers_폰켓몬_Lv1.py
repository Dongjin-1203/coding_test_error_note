"""
[문제] 1845 - 폰켓몬
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/1845
[패턴] 해시(딕셔너리)
[난이도] Lv.1
[풀이시간] 23분
[재도전여부] N  # 처음 못 풀었으면 Y

[접근법]
- 리스트 요소의 종류의 수가 중요하다. Counter, set을 적절히 활용해보자.

[시간복잡도] O(N)
[공간복잡도] O(N)

[실수/배운점]
- 본질을 파악해 불필요한 로직을 줄이는 노력이 필요함
- 불필요한 함수 사용은 고민을 해봐야 한다. Counter는 요소의 개수를 세는 데 유용하지만, 이 문제에서는 종류의 수를 세는 것이 중요하기 때문에 set을 사용하는 것이 더 간단하고 효율적임.
"""


# ====== 문제 파악 ======
# 1. nums 배열의 각 요소는 폰켓몬 종류의 고유번호이다.
# 2. N/2마리의 폰켓몬을 선택해야 한다.
# 3. 같은 종류의 폰켓몬만 선택할 수도 있다.(Counter를 사용해야할 수 있음)
# 4. 여러가지 경우의 수 중에 가장 많은 종류를 선택할 수 있는 방법을 찾아야함.
# 5. 다양한 종류의 폰켓몬을 선택해야하면 각각 종류의 폰켓몬을 하나씩 선택하는 방식으로 풀이.

# ====== 로직 설계 ======
# 1. Counter로 nums 배열의 요소들을 세어서 종류별로 몇 마리씩 있는지 파악한다.
# 2. 몇마리를 선택해야 하는지 계산한다.(len(nums) // 2)
# 3. 한마리씩 빼면 그 종류의 포켓몬 번호를 리스트에 담는다.
# 4. Counter에서 1마리씩 선택해서 len(nums) // 2마리가 선택이 완료되면 종료한다.
# 5. 선택된 포켓몬 번호의 종류의 수를 세어서 반환한다.

from collections import Counter

def solution(nums):
    count = Counter(nums)
    selected = []

    while len(selected) < len(nums) // 2:
        for key in count:
            if len(selected) < len(nums) // 2:
                selected.append(key)
                count[key] -= 1

    selected = set(selected)
    answer = len(selected)
    return answer

if __name__ == "__main__":
    nums = [3,1,2,3]
    print(solution(nums))