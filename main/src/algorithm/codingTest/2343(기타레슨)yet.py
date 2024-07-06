N,M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
left, right = max(arr), sum(arr)
print(left,right)
while left <= right:
    mid = (left+right)//2
    # 블루레이에 강의 넣기
    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)

# https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2343%EB%B2%88-%EA%B8%B0%ED%83%80-%EB%A0%88%EC%8A%A8-%ED%8C%8C%EC%9D%B4%EC%8D%AC

