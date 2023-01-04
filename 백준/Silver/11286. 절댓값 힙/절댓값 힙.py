import sys
input = sys.stdin.readline
import heapq

hip = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(hip) == 0: # 리스트가 비어있으면
            print(0) # 0 출력
        else:
            print(heapq.heappop(hip)[1])# 최솟값 출력후 삭제하기
    else:
        heapq.heappush(hip, (abs(m), m))
