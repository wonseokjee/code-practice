T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[1]+[0]*(N-1) for _ in range(N)]
    di=[-1,-1]#방향판 상, 좌상
    dj=[0,-1]
    len_i = len(di)
    for i in range(1,N):
        arr_result = []
        for j in range(1,N):
            for k in range(len_i):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] !=0:
                        arr[i][j] += arr[ni][nj]
    arr_result = []
    for a in range(N):
        arr_result.append(arr[a][0:a+1])
    print(f'#{tc}')
    for a in arr_result:
        for b in a:
            print(b, end=' ')
        print()
