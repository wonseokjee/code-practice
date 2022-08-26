N, K = map(int, input().split())

arr=[[0,0] for _ in range(7)]
#학년, 성별순 0(여학생),1(남학생) ex) arr[1][0] 1학년 여학생
room = 0
for i in range(N):
    gender,grade = map(int, input().split())
    arr[grade][gender] += 1
for j in range(1,7):
    for l in range(2):
        if 0<arr[j][l] < K:
            room += 1
        else:
            if arr[j][l]%K == 0:
                room += arr[j][l] // K
            else:
                room += (arr[j][l]//K)+1
print(room)