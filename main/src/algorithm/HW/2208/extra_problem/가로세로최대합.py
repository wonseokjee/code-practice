T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d = []
    len_d = 4 * (N-1)
    for direct in range(1, N):                  #가로 세로 길이가 N*2인 방향판 생성
        d.append([direct, 0])
        d.append([-direct, 0])
        d.append([0, direct])
        d.append([0, -direct])
    cnt_max = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(len_d):
                ni = i + d[k][0]
                nj = j + d[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += arr[ni][nj]          # 방향판을 곱한 범위안의 값을 cnt에 덧셈
            cnt += arr[i][j]                    # 자기자신 덧셈
            if cnt > cnt_max:
                cnt_max = cnt

    print(f'#{tc} {cnt_max}')