N = list(map(int, input()))

cnt_0 = 0
cnt_1 = 0
k = 0
for i in range(len(N)): # 0과 1중 개수가 적은 것을 찾기
    if N[i] == 1:
        cnt_1 += 1
    else:
        cnt_0 += 1
if cnt_1 >= cnt_0:
    k = 1
cnt = []
result = 0
for j in range(len(N)):
    if N[j] == k: #개수가 적은 것이면 리스트에 추가
        cnt.append(k)
    else:
        if 0 <= j-1 < len(N): #인덱스 에러 방지
            if N[j-1] != k: #이전숫자가 k가 아니고 같은숫자이면
                continue
            else: #이전것이 다른 숫자 이면 리스트 초기화 후 카운트
                result += 1
                cnt = []
print(result)