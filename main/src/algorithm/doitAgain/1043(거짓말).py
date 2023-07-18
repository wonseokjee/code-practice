from collections import deque
n,m = map(int, input().split())
know = list(map(int, input().split()))
know.pop(0)
party = [0] * m
queue = deque(know)
arr = []
for i in range(m):
    a, *arg = map(int, input().split())
    # print(arg)
    arr.append(arg)
while(queue):
    x = queue.popleft()
    for i in range(m):
        if x in arr[i]:
            party[i] += 1
            for j in arr[i]:
                if not j in know:
                    know.append(j)
                    queue.append(j)
# print(party)
print(party.count(0))
