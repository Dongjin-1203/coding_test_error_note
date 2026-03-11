"""
[문제] 42577 - 전화번호 목록
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42577
[패턴] 해시(딕셔너리)
[난이도] Lv.2
[풀이시간] 25분
[재도전여부] Y  # 처음 못 풀었으면 Y

[접근법]
- 번호 리스트를 정렬해서 비교하는 것이 제일 간단하다. 어떤 식으로 정렬할지 고민해보자.

[시간복잡도] O(nlogn)
[공간복잡도] O(1)

[실수/배운점]
- 사전순 정렬이 가장 간편하다. 사전순으로 정렬하면 접두사와 유사한 번호는 인접에 위치하게 된다.
- 길이 기준 정렬 후 모든 쌍을 비교하면 O(n²)이 되어 n=100만에서 TLE가 발생한다. 따라서 길이 기준 정렬은 적절하지 않다.
"""

# ====== 문제 파악 ======
# 1. 어떤 전화번호가 다른 전화번호에 시작 부분에 있는 경우가 있는지 확인해야 한다.
# 2. 전화번호가 다른 전화번호의 접두어인 경우가 있는지 확인해야 한다.
# 3. 전화번호가 다른 전화번호의 접두어인 경우가 있으면 false를 반환해야 한다.
# 4. 제일 짧은 번호를 기준으로 n번째(인덱스) 번호가 비교하는 번호를 포함하는지 확인하면 될 것 같다.

# ====== 로직 설계 ======
# 1. 전화번호를 길이순으로 정렬한다.
# 2. 제일 짧은 번호를 기준으로 n번째(인덱스) 번호가 비교하는 번호를 포함하는지 확인한다.(for문으로 비교)
# 3. 포함된다면 false를 반환한다.

"""
def solution(phone_book):
    answer = True
    sorted_phone_book = sorted(phone_book, key=lambda x: len(x))
    number = sorted_phone_book.pop()

    for i in range(len(sorted_phone_book)):
        if number.startswith(sorted_phone_book[i]):
            answer = False
            break

    return answer
"""

# ====== 문제 분석 ======
# 1. number = sorted_phone_book.pop()  # 가장 긴 번호 하나만 꺼냄
# 2. 길이 기준 정렬 후 모든 쌍을 비교하면 O(n²)이 되어 n=100만에서 TLE
# 3. 사전순 정렬이 가장 간편함.
# 4. 사전순으로 정렬하면 접두사와 유사한 번호는 인접에 위치하게됨.

def solution(phone_book):
    phone_book.sort()  # 사전순 정렬 (길이순 X)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

if __name__ == "__main__":
    phone_book = ["12","123","1235","567","88"]
    

    print(solution(phone_book))