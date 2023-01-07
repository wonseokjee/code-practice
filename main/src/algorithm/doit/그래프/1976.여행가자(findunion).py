# 서로소 집합(union find)

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v = int(input())
e = int(input())
parent = [0] * (v + 1)
lst = []
# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(v):
    node = list(map(int, input().split()))
    for j in range(v):
        if node[j]:
            lst.append([i+1,j+1])
plan = list(map(int, input().split()))
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    # if parent[x] != x:
    #     return find_parent(parent, parent[x])
    if parent[x] == x:
        return x
    p = find_parent(parent, parent[x])
    parent[a] = p
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# union 연산을 각각 수행
for i in range(len(lst)):
    a, b = lst[i][0], lst[i][1]
    union_parent(parent, a, b)

ans = set()
for j in range(len(plan)):
    ans.add(find_parent(parent, plan[j]))
print('YES' if len(ans) == 1 else 'NO')

# print(ans)
# print(lst)
# print(parent)


# 5
# 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 5

