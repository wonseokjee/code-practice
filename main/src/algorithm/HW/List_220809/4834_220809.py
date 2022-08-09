T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    # arr 원소에 대한 카운트 배열 만들기(숫자 카드 0~9 장수 세기)
    num_cnt = [0]*10 # 0~9 10개의 숫자에 대해
    # 배열에 숫자따른 장수를 num_cnt에
    for i in arr:
        num_cnt[i] += 1 
    # cnt에서가장 많은 카드 찾기
    max_cnt = 0
    for j in range(10):
        if num_cnt[j] >= max_cnt:
            max_cnt = num_cnt[j] # 가장 큰 숫자를 max_cnt에 저장했을때
            num = j # 그때의 숫자
    print(f'#{tc} {num} {max_cnt}')