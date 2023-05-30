n,h = map(int, input().split())
bottom=[0]*n
top=[0]*n
ans = [0]*h
for i in range(1,n+1):
    if i%2==1:
        bottom[i-1] = int(input())
    else:
        top[i-1] = int(input())
# print(bottom,top)

for j in bottom:
    for k in range(j):
        ans[k] += 1
for l in top:
    for m in range(h-1,h-l-1,-1):
        ans[m]+=1
# print(ans)
ans_min = min(ans)
ans_min_cnt = ans.count(ans_min)
print(ans_min, ans_min_cnt)
