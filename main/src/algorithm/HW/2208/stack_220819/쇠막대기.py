T = int(input())
for t in range(1, T + 1):
    arr = input()

    stick = 1  # 쌓인 쇠막대기 개수
    pieces = 0  # 잘려진 조각 개수

    for i in range(1, len(arr)):
        if arr[i] == '(':
            stick += 1  # 열린 괄호, 막대 개수  +1


        else:
            stick -= 1  # 닫힌 괄호, 막대 개수 -1
            if arr[i - 1] == '(':  # 직전에 열린 괄호였다면, 레이저.
                pieces += stick  # 막대 개수만큼 조각 +
            else:
                pieces += 1  # 아니면, 막대기 끝점. 막대 개수 +1

    print(f'#{t} {pieces}')
