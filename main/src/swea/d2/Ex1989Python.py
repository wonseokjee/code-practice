##초심자의 회문 검사 
##점프투파이썬 회문 판별 함수 만들기 4.1.1
import sys
##txt파일 읽기
sys.stdin = open(
    'd:/spring_inflearn/code-practice/main/src/swea/d2/Ex1989Python.txt', 'r')

##작업 경로 확인하기
""" import os
print(os.getcwd()) """

t = int(input())
a = range(t)

for i in range(0,t):
    pal = input()
    a = pal[::-1].lower()##문자열 거꾸로 돌리고 소문자로
    if pal == a:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')

#완료
