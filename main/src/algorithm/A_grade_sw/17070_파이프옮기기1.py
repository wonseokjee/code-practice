#파이프가 두개의 칸 차지하고 두개의 칸이 가로인지 세로인지 대각인지에 따라
#미리 7개의 방향판ㄹ만들어 놓고 bfs? 가로에 2개 세로에 2개 대각에 3개
#파이프를 큐로
from collections import deque

N = int(input())
arr = [map(int, input().split()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
garo = [[0,1],[1,1]]
sero = [[1,0],[1,1]]
daegak = [[0,1],[1,0],[1,1]]
def bfs(visited,x):
    queue = deque([[1,1],[1,2]])
    while(queue):



