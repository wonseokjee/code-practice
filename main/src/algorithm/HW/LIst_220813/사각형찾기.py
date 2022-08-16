import sys
sys.stdin = open('사각형찾기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+2)]+[[0] + list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]
    cnt_max = 0    # 최대값
    cnt_both = 0    # 최대값 비교
    for i in range(N):
        cnt_length = 0  # 가로
        for j in range(N):
            cnt_height = 0  # 세로
            cnt_both = 0  # 곱한 값 비교
            if arr[i][j] == 1:
                cnt_length += 1
                if arr[i][j+1] == 0:
                    x = i #세로로 내려갈 값.
                    while x < N+1: #indexerror 방지
                        if arr[x][j] == 0:
                            cnt_both = cnt_height * cnt_length
                            if cnt_max < cnt_both:
                                cnt_max = cnt_both
                                break
                        if arr[x][j] == 1:
                            cnt_height += 1
                        x += 1
    print(f'#{tc} {cnt_max}')


