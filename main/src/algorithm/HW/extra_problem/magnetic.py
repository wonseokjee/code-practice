import sys
sys.stdin = open('magnetic_1.txt', 'r')

# T = 10
# for tc in range(1,T+1):
N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
#1은 내리고 2는 올리고
#1은 아래부터 검색 2는 위부터 검색
#1검색
