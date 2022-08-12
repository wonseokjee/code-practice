T = int(input())
for tc in range(1,T+1):
    N = int(input())
    position = [set({}),set({})]
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                position[color-1].add((a, b))
    # print(position)
    result_in = position[0] & position[1]

    print(f'#{tc} {len(result_in)}')

