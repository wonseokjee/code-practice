N = int(input())
arr = [0]*366
ans = []
for _ in range(N):
    x,y = map(int, input().split())
    for i in range(x,y+1):
        arr[i] += 1
wid = 0
leng = 0
for i in range(1,366):
    if arr[i] > 0:
        wid += 1
        if arr[i]> leng:
            leng = arr[i]
    if arr[i]==0 and arr[i-1]>0:
        ans.append(wid*leng)
        wid = 0
        leng = 0
if wid>0 and leng>0:
    ans.append(wid * leng)
print(sum(ans))