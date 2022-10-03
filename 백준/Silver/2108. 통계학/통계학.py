import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
cnt = [0]*8001
sm = sum(arr)/N # 산술평균
print(round(sm))
mid = arr[N//2] # 중앙값
print(mid)
for i in arr:
    cnt[4000+i] += 1
x = max(cnt)
if cnt.count(x) == 1:
    y = cnt.index(x)
else:
    d = cnt.index(x)
    cnt[d] = 0
    y = cnt.index(x)
print(y-4000) #최빈값

ran = max(arr)-min(arr) # 범위
print(ran)