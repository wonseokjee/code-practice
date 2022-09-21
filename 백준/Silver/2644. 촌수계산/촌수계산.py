from collections import deque

n = int(input()) #  전체 사람의 수
m1, m2 = map(int, input().split())
node = int(input())
# 1.트리 만들기
lst = [[]*(n+1) for _ in range(n+1)]
for _ in range(node):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
# print(lst)
# 2.사람수와 같은 길이의 리스트 생성
distance = [-1 for _ in range(n+1)]
# 3.bfs 설계
def bfs(v):
    distance[v] = 0
    queue = deque()
    queue.append(v)
    while queue:
        # print(queue)
        i = queue.popleft()
        # print(i)
        for k in lst[i]:
            if distance[k] == -1:
                distance[k] = distance[i] + 1 #같은 bfs 수준에 같은 숫자
                queue.append(k)

bfs(m1)
print(distance[m2])
# distance[m2] 가 답임