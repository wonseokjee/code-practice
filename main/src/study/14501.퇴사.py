n = int(input())
arr_time = [0]
arr_value = [0]
arr_check =[0]*(n+1)
for i in range(1,n+1):
    x,y = map(int, input().split())
    arr_time.append(x)
    arr_value.append(y)
def dfs(x,visited, cnt):
    time_cnt = x + arr_time[x]
    if time_cnt <= n+1:
        cnt += arr_value[x]
        # print(x, cnt, time_cnt)
        if arr_check[x]<cnt:
            arr_check[x]=cnt
            for k in range(time_cnt, n+1):
                if k + arr_time[k] <= n+1:
                    dfs(k,visited,cnt)

for j in range(1,n+1):
    dfs(j,arr_check, 0)
print(max(arr_check))
