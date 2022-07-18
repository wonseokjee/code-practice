##직사각형에서 탈출

import sys
##txt파일 읽기
sys.stdin = open(
    'd:/spring_inflearn/code-practice/main/src/solvedAc/bronze3/Ex1085.txt', 'r')

##작업 경로 확인하기
""" import os
print(os.getcwd()) """
a = range(0,4)
for i in a:
    """
    graph = list(map(int,input().split()))
    #print(graph)
    a = graph[2] - graph[0]
    b = graph[3] - graph[1]
    num = [graph[0],graph[1],a,b]
    sort = sorted(list(map(int, num)))
    print(sort[0])
    """
    x, y, w, h = map(int, input().split(" "))
    print(min(x, y, w-x, h-y))


    
