N = int(input())
arr = [list(input().split())for _ in range(N)]
arr.sort(key=lambda x:x[1])
print(type(arr[0][1]))
for i in range(N):
    print(arr[i][0],end=' ')

# sort(key=lambda x:x[1])에서 x[1]을 int형으로 변환하지 않을 경우
# ascii 코드로 변환됨
# 숫자의 경우에는 첫째자리에서 판단 두번째 자리에서 판단
# 테케의 백장가 - 홍길동 - 이가람 순임
# 첫째자리 우선순위 판단후 둘째자리 판단함
# 결과 : 백장수 - 이순신 - 백장가 - 홍길동 - 이가람 - 지원석


# 6
# 홍길동 95
# 이순신 77
# 이가람 9b
# 지원석 b
# 백장수 !
# 백장가 9!