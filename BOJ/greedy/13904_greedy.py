import sys
import heapq
sys.stdin = open("BOJ\\greedy\\input5.txt",'r')
input = sys.stdin.readline
array = []
# 문제에서 n<= 1000이기 때문
visit = [False] * 1001

# 갯수 받기
n = int(input())

for i in range(n):
    d, s = map(int,input().split())
    array.append((d,s))
array.sort(key = lambda x : x[1], reverse =True)

answer = 0

for day, score in array:
    # 각 점수마다 내림차순 했으므로 그 날짜 값에 해당 되는 값을 우선적으로 넣음
    i = day
    while i > 0 and visit[i]:
        i -= 1
    # 해당되는값 없으면 패스
    if i == 0:
        continue
    else:
        visit[i] = True
        answer += score
print(answer)