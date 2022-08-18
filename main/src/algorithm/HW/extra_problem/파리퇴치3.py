T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_cross = []
    arr_X = []
    catch_len = (M-1)*4
    catch_max = 0
    for a in range(1, M):
        arr_cross += [[a, 0]] + [[-a, 0]] + [[0, -a]] + [[0, a]]
        arr_X += [[a, a]] + [[-a, -a]] + [[a, -a]] + [[-a, a]]
    for i in range(N):
        for j in range(N):
            cross_sum = arr[i][j]
            X_sum = arr[i][j]
            for cross in range(catch_len):
                ni = i + arr_cross[cross][0]
                nj = j + arr_cross[cross][1]
                if 0 <= ni <N and 0 <= nj <N:
                    cross_sum += arr[ni][nj]
            for X in range(catch_len):
                di = i + arr_X[X][0]
                dj = j + arr_X[X][1]
                if 0 <= di < N and 0 <= dj < N:
                    X_sum += arr[di][dj]
            if cross_sum > catch_max:
                catch_max = cross_sum
            if X_sum > catch_max:
                catch_max = X_sum

    print(f'#{tc} {catch_max}')