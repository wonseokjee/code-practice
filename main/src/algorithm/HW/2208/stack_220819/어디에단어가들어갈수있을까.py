import sys
sys.stdin = open('어디에단어가들어갈수있을까.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    #가로 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] : # 1이면 true 취급되서 통과
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0 #0으로 막혀서 cnt초기화
        if cnt == K:
            result += 1
    #세로찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] : # 1이면 true 취급되서 통과
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
    print(f'#{tc} {result}')