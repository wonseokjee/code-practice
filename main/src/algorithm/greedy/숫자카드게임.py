N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
grp = [] # 비교할 list
for i in range(N):
    grp.append(arr[i]) #grp list에 삽입
    if len(grp) == arr[i]: #grp 길이와 arr[i]숫자가 같으면(오름차순이라 가능)
        cnt += 1           # count
        grp = []           # grp 초기화

print(cnt)

# 5
# 2 3 1 2 2