N = int(input())
for tc in range(N):
    result = [[0,0] for _ in range(5)]#행= 0비우고 각 숫자별 딱지 개수 ,열= A,B
    A, *game_A = map(int, input().split())#A와 A의 딱지
    B, *game_B = map(int, input().split())
    len_put = len(game_A) if len(game_B)<len(game_A)else len(game_B) #길이가 서로 달라서 가장 긴 길이 선택
    for i in range(len_put):
        if 0 <= i < len(game_A):#서로 길이가 달라서 범위 제한
            result[game_A[i]][0] += 1 #숫자별 딱지 개수 세기
        if 0 <= i < len(game_B):
            result[game_B[i]][1] += 1
    win = ''
    for j in range(4,0,-1):

        if result[j][0] > result[j][1]:
            win = 'A'
            break
        elif result[j][0] < result[j][1]:
            win = 'B'
            break
        else:
            if j == 1:
                win='D'
            continue
    print(win)
