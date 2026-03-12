"""
[문제] 42578 - 의상
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42578
[패턴] 해시(딕셔너리)
[난이도] Lv.2
[풀이시간] 27분
[재도전여부] N # 처음 못 풀었으면 Y

[접근법]
- 곱의 법칙 적용
- conter 모듈을 사용해서 카테고리별 의상 개수를 세어서 딕셔너리에 저장

[시간복잡도] O(n)
[공간복잡도] O(1)

[실수/배운점]
- 안입는 것을 포함해서 곱의 법칙을 적용해야 한다. (count + 1)
"""
# ====== 문제 파악 ======
# 1. 2차원 배열로 0번 인덱스는 의상, 1번 인덱스는 카테고리이다.
# 2. 카테고리에는 1개 이상의 의상이 있다.
# 3. 서로 다른 옷의 조합의 수를 구해야 한다.
# 4. 최소 1개는 입어야한다.
# 5. 1개만 입을때 2개만 입을때 3개만 입을때 ... n개만 입을 때의 조합의 수를 구해서 더하면 될 것 같다.
# 6. 조합의 수를 구하는 것을 구현하는 것이 핵심일 것 같다.

# ====== 로직 설계 ======
# 1. 카테고리별로 의상의 개수를 세어서 딕셔너리에 저장한다.
# 2. 1개만 입을 때 2개만 입을 때 ... n개만 입을 때의 경우의 수를 구한다.

from collections import Counter

def solution(clothes):
    category_count = Counter(category for _, category in clothes)
    answer = 1
    for count in category_count.values():
        answer *= (count + 1)
    return answer - 1

if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))