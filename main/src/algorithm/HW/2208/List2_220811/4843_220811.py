T = int(input())
for tc in range(1, T+1):
    size = int(input())
    arr = list(map(int, input().split()))
    result = []
    for i in range(len(arr)):                   #배열의 크기만큼 반복 버블정렬
        for j in range(size-i-1):               #끝은 정렬이 끝났으므로 하나씩 빼면서 순환
            if arr[j] > arr[j+1]:               #앞의 idx가 더 크다면 바로 다음idx와 변경
                arr[j], arr[j+1] = arr[j+1], arr[j]
    while len(arr) != 0:
        result.append(arr[-1])
        del arr[-1]
        result.append(arr[0])
        del arr[0]
    result_ten = result[:10]
    print(f'#{tc} {" ".join(map(str,result_ten))}')