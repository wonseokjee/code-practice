n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
num = 0
while(arr):
    # 작은 순대로 정렬한 arr를 pop한다.
    x = arr.pop()
    #x가 2보다 큰 경우, 하나 더 pop해서 곱한다.
    if x > 2:
        if arr:
            y = arr.pop()
            if y >= 2:
                num += x*y
            else:
                num += x
                arr.append(y)
    #x가 2,1 인 경우, 그냥 값에 더해준다.
    if x ==2 or x==1:
        num += x
    #x가 0인 경우 남은 arr이 짝수이면 그냥 버리고,
    if x ==0:
        if len(arr) % 2 == 1:
            y = arr.pop()
    if x < 0:
        if len(arr) % 2 == 0:
            num += x
        else:
            y = arr.pop()
            num += x*y


print(num)