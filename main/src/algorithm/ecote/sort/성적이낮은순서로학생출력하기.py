N = int(input())
arr = [list(input().split())for _ in range(N)]
arr.sort(key=lambda x:x[1])
for i in range(N):
    print(arr[i][0],end=' ')


# 3
# 홍길동 95
# 이순신 77
# 이가람 99