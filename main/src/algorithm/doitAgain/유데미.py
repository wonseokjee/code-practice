def solution(m, n, board):
    answer = 0
    # 2x2 돌면서 모두 같은지 판단하는 함수
    board_splt = []
    for k in board:
        board_splt.append(list(k))
    # print(board_splt)
    check = True
    while (check):
        erasor = []
        for i in range(m - 1):
            for j in range(n - 1):
                current_block = board_splt[i][j]
                if not current_block == 0:  # 현재 블록이 0이 아닐경우
                    address = [[i, j]]
                    for dx, dy in (0, 1), (1, 0), (1, 1):
                        x = i + dx
                        y = j + dy
                        if current_block == board_splt[x][y]:
                            address.append([x, y])
                    if len(address) == 4:
                        for x, y in address:
                            erasor.append([x, y])
        # print(erasor)
        # 2x2가 같으면 주소값을 임시저장(일단 모두 임시저장하고 같으면 저장)
        # 같은 것이 없을 때 종료

        # 저장된 주소값을 지우는 함수
        if len(erasor) > 0:
            for l, r in erasor:
                board_splt[l][r] = 0
            print(board_splt)
        else:
            check = False

        # 빈칸이 아닐때까지 밑으로 내리는 함수
        for a in range(m - 2, -1, -1):
            for b in range(n):
                c = a
                # print(board_splt[c][b],c,b)
                while (True):
                    if board_splt[c][b] != 0 and board_splt[c + 1][b] == 0:
                        # if board_splt[c][b].isalpha():
                        # print(board_splt[c][b],c,b)
                        board_splt[c + 1][b] = board_splt[c][b]
                        board_splt[c][b] = 0
                        c += 1
                    else:
                        break
        print(board_splt)

    # 빈칸의 갯수를 세는 함수

    return answer

# lst1= ["1 2 3 4 B B 42 B F F", "1 10 B B 20 1 F B B"]
# for i in lst1:
#     solutions(i)
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
m = 4
n = 5
solution(m,n,board)
