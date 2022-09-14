import sys
sys.stdin = open('배열최소합.txt', 'r')

def checknode(depth, cnt_sum):
    global cnt_min
    if cnt_sum > cnt_min: #cnt_sum이 cnt_min보다 크면 확인할 필요 없음. 유망성 감사
        return #아무것도 return 안하고 종료.
    if depth == N: #depth가 끝행에 도달하면
        if cnt_sum < cnt_min:#cnt_sum이 작으면
            cnt_min = cnt_sum#cnt_sum을 최소값으로
        return
    else:
        for j in range(N): #열 검사.
            if not column_visited[j]:#column_visited가 true가 아니면
                column_visited[j] = True #true로 바꾸고, 열 중복방지
                checknode(depth+1, cnt_sum+arr[depth][j]) #재귀 , 다음 행에 cnt_sum을 더해서 가지고 간다.
                column_visited[j] = False #재귀로 찾지 못했으면 다시 false로.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    column_visited = [False] * N #같은 행에 중복 방지
    cnt_min = 101 #최대합 100이고, 최소값 찾기
    checknode(0,0)
    print(f'#{tc} {cnt_min}')








