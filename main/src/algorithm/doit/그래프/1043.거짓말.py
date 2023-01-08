n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


def find(parent, x):
    if parent[x] == x:
        return x
    p = find(parent, parent[x])
    parent[x] = p
    return parent[x]

def union_find(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


know_count, *know_people = map(int, input().split())
if know_count > 0:
    know_root = min(know_people)
    for i in know_people:
        parent[i] = know_root

party = []
for i in range(m):
    people_count, *people = map(int, input().split())
    party.append([*people])
    if people_count > 1:
        for j in range(people_count-1):
            union_find(parent, people[j], people[j+1])
print(parent)
print(party)
ans = 0
if know_count > 0:
    root_number = parent[know_root]
    for i in party:
        for j in i:
            if parent[j] != root_number:
                ans += 1
                break
else:
    ans = m
print(ans)

# 9 4
# 1 1
# 4 1 2 3 4
# 4 5 6 7 8
# 2 8 9
# 2 4 9