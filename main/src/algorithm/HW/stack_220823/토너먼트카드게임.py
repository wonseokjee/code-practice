import sys
sys.stdin = open('토너먼트카드게임.txt', 'r')

def win(left, right):
    if (num[left-1] - num[right-1] == 1 ) or (num[left-1] - num[right-1]==-2) or (num[left-1] - num[right-1]==0) :
        return left
    else:
        return right

def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾아 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int, input().split()))
    print(f'#{tc} {f(1,N)}')




