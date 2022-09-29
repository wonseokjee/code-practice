# 국어점수가 높은 순서
# 같으면 영어점수가 낮은 순서
# 같으면 수학점수가 높은 순서
# 모두 같으면 알파벳순서.
N = int(input())
arr = []
for _ in range(N):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    arr.append([name,kor,eng,math])
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
print(arr)
