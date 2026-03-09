"""
[문제] 42583 - 다리를 지나는 트럭
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42583
[패턴] 스택/큐
[난이도] Lv.2
[풀이시간] 50분
[재도전여부] Y  # 처음 못 풀었으면 Y

[접근법]
- 

[시간복잡도] O(N × bridge_length)
[공간복잡도] O(bridge_length)

[실수/배운점]
- 문제의 조건을 잘못 파악해서 트럭이 정해진 순서에 따라 다리를 건너야 하는데, 무게가 가벼운 트럭부터 보내는 로직을 짜서 틀렸음.
- bridge_length 만큼의 큐를 만들어서 트럭이 다리를 건너는 과정을 시뮬레이션하는 방식으로 풀이.
"""

# ====== 문제 파악 ======
# 1. 한 번에 지날 수 있는 차량 대수가 있다.(bridge_length)
# 2. 다리가 견딜 수 있는 최대 무게가 있다.(weight)
# 3. 트럭이 다리를 건너는 데 걸리는 시간은 1초이다.
# 4. 트럭이 다리를 건너는 데 걸리는 시간은 bridge_length
# 5. 트럭 무게 리스트(truck_weights)의 순서는 크게 상관 없다. 
# 6. 내림차순으로 정렬 시키고 무거운 차부터 보내어 최적의 결과를 얻는다.
# 7. 트럭이 다리위에 올라오는 것도 1초 계산. 빠지는 것도 1초 계산 해야한다.

# ====== 로직 설계 ======
# 1. truck_weights를 내림차순으로 정렬한다.
# 2. 제일 앞의 요소를 뽑는다.(+1)
# 3. 뽑은 요소와 다음 요소의 합이 weight보다 작거나 같으면 다음 요소도 뽑는다.(+1)

"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.sort(reverse=True)
    on_bridge = []

    while truck_weights:
        answer += 1
        current_truck = truck_weights.pop(0)
        on_bridge.append(current_truck)

        if truck_weights and truck_weights[0]<= weight-current_truck:
            current_truck = truck_weights.pop(0)
            on_bridge.append(current_truck)
        if weight - sum(on_bridge) <= 0:
            on_bridge.pop(0)
            answer += 1
        answer += bridge_length - 1
    return answer
"""
"""
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.sort(reverse=True)
    on_bridge = deque()


    while truck_weights:
        answer += 1
        current_truck = truck_weights.pop(0)
        on_bridge.append(current_truck)

        print(f"남은 무게: {weight-sum(on_bridge)}")
        if truck_weights and truck_weights[0] <= weight-sum(on_bridge):
            current_truck = truck_weights.pop(0)
            on_bridge.append(current_truck)
            answer += 1
        else:
            exit_truck = on_bridge.popleft()
            answer += 1
            weight += exit_truck -1
            print(f"다리에서 빠지는 트럭: {exit_truck}, 현재 다리 위 트럭: {on_bridge}")

        print(answer, on_bridge)
    return answer
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리를 큐로 표현
    current_weight = 0
    time = 0
    idx = 0  # 다음 올라올 트럭 인덱스

    while idx < len(truck_weights):
        time += 1
        exiting = bridge.popleft()       # 다리 앞에서 나가는 트럭
        current_weight -= exiting

        next_truck = truck_weights[idx]
        if current_weight + next_truck <= weight:  # 올라올 수 있으면
            bridge.append(next_truck)
            current_weight += next_truck
            idx += 1
        else:
            bridge.append(0)             # 빈 자리로 채움

    time += bridge_length  # 마지막 트럭이 다 건너는 시간
    return time

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weights))