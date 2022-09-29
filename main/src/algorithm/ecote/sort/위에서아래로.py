#수열을 내림차순으로 정렬하는 프로그램을 만드시오
#계수정렬로 풀기
N = int(input())
arr = [0]*100001
for _ in range(N):
    a = int(input())
    arr[a] += 1
for i in range(len(arr)-1,-1,-1):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i,end=' ')
