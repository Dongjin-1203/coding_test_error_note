"""
[문제] BOJ 1753 - 최단경로
[링크] https://www.acmicpc.net/problem/1753
[패턴] 다익스트라
[난이도] Gold IV
[풀이시간] 35분
[재도전여부] Y  # 처음 못 풀었으면 Y

[접근법]
- heapq 기반 다익스트라
- 핵심 인사이트: 방문 처리를 pop 시점에 해야 함

[시간복잡도] O((V + E) log V)
[공간복잡도] O(V + E)

[실수/배운점]
- dist 초기화를 float('inf')로 안 해서 런타임 에러
"""