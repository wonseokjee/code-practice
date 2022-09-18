import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N+1)]
track=[0]*(N+1)

def dfs(n):
    if track[n] ==0:
        track[n] = 1
        # print(f'{n}-',end='')
        ins.append(n)
        for j in range(len(arr[n])):
            dfs(arr[n][j])
    else:
        pass
        # print(n)
        ins.append(n)

for i in range(1,N):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
ins = []
result = [0]*(N-1)
print(arr)

dfs(1)
print(ins)
for k in range(1,len(ins),2):
    result[ins[k]-2] = ins[k+1]
# print(result)
for a in result:
    print(a)