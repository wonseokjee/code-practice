##중간값 찾기
import sys
##txt파일 읽기
sys.stdin = open(
    'd:/spring_inflearn/code-practice/main/src/swea/d1/Ex2063Python.txt', 'r')

##작업 경로 확인하기
""" import os
print(os.getcwd()) """
N = int(input())
N_list = sorted(list(map(int,input().split())))
print(N_list[N//2])

##완료

