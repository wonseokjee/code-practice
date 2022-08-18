T = int(input())
for tc in range(1,T+1):
    N = int(input())
    position = set({})
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for a in range(x1,x2+1):
            for b in range(y1, y2+1):
                position.add((a,b))
    print(f'#{tc} {len(position)}')