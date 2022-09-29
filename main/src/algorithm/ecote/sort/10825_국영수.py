# 국어점수가 높은 순서
# 같으면 영어점수가 낮은 순서
# 같으면 수학점수가 높은 순서
# 모두 같으면 알파벳순서.
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())
arr.sort(key=lambda x:int(x[1]),reverse=True)

