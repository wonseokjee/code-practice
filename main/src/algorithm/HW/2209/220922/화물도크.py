import sys
sys.stdin = open('화물도크.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1])) #  종료시간이 가장 짧은 것부터 입력
    work = ['0'] * 26
    def dfs(n,num,work): #cnt 안되는 것을 세어서 최소값보다 크면 패스
        global cnt
        if n == N:
            if num < cnt:
                cnt = num
            return
        if '1' in work[arr[n][0]:arr[n][1]]:
            num += 1
        else:
            for i in range(arr[n][0],arr[n][1]):
                work[i] = '1'
        dfs(n+1,num,work)

    dfs(0,0,work)
    print(f'#{tc} {N-cnt}')