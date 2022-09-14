# import sys
# sys.stdin = open('색칠하기2.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    position = [set({}), set({})]
    x_max = y_max = 0
    x_min = y_min = 10
    position_sep = [set({map(int, range(N))})]
    print(position_sep)
    position_sep_result = []
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for a in range(x1, x2+1): # a,b에 해당하는 좌표 생성
            for b in range(y1, y2+1):
                position[color-1].add((a,b)) #postion - set에 넣기 -> 여기서 같은색 구분해야.
                if x_max < a:
                    x_max = a
                elif x_min > a:
                    x_min = a
                if y_max < b:
                    y_max = b
                elif y_min > b:
                    y_min = b
                position_sep[i].add((a,b))
        result_in = position[0] & position[1]
    for j in range(N):
        for k in range(N):
            position_sep_result = (position_sep[j] & position_sep[k-j])


    # print(position_sep_result)
    # print(x_min, x_max, y_min, y_max)
    result_out = ((x_max-x_min+1) + (y_max-y_min+1))*2
    # print(result_in)
    # print(result_out)
    # print((len(result_in))*2 + result_out)
    #같은색 두개를 분리해서 다른색과 각각 비교