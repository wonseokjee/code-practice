T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        pal_down = []  # 세로 찾기 리스트
        pal_right = [] #가로 찾기 리스트
        for j in range(N):
            pal_down.append(arr[j][i])
            pal_right.append(arr[i][j])
        k = 0
        down = ''.join(pal_down)
        right = ''.join(pal_right)
        while N - k >= M:
            right_slice = right[k:M+k]
            down_slice = down[k:M+k]
            if right_slice == right_slice[::-1]: #가로 회문 찾기
                print(f'#{tc} {right_slice}')
            if down_slice == down_slice[::-1]: #세로 회문 찾기
                print(f'#{tc} {down_slice}')
            k += 1





