import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
cnt = 0
while len(arr)>1:
    num = arr.pop()
    if m-num in arr:
        cnt += 1
print(cnt)