T=10
for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    ch1 = [0]*100   #from인덱스 to 원소
    ch2 = [0]*100
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1] #a,b를 두개씩 읽는 것.
        adjList[a].append(b)
        # if ch1[a] == -1: #a의 첫번째 도착지
        #     ch1[a] = b
        # else:
        #     ch2[a] = b
def dfs(v, N):
    visited = [0] * 100
    stack = [0] * 100
    top = -1
    # print(v)            # 방문
    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            #push(v);
                stack[top] = v
                v = w               # v  w;  (w에 방문)
                # print(v)  # 방문
                if v == 99:
                    return 1
                visited[w] = 1      # visited[w] true;
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]          # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while
    return 0