##1대1 가위바위보
import sys
##txt파일 읽기
sys.stdin = open(
    'd:/spring_inflearn/code-practice/main/src/swea/d1/Ex1936Python.txt', 'r')

##작업 경로 확인하기
import os
print(os.getcwd())

""" count = str(input())
print(count)
a = int(count[0])
b = int(count[2]) """
a,b = map(int, input().split()) 

if a-b==(1 or -2):
    print('A')
elif a-b==(2 or -1):
    print('B')

##완료





