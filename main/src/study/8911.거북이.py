T = int(input())
for tc in range(1,T+1):
    turtle = input()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = 0,0
    direct=0
    minusX, minusY, plusX, plusY = 0,0,0,0
    for i in turtle:
        if i == 'R':
            direct += 1
        elif i == 'L':
            direct -= 1
        elif i == 'F':
            x += dx[direct%4]
            y += dy[direct % 4]
        elif i == 'B':
            x -= dx[direct%4]
            y -= dy[direct % 4]

        if x > 0 and x > plusX:
            plusX = x
        elif x < 0 and x < minusX:
            minusX = x

        if y > 0 and y > plusY:
            plusY = y
        elif y < 0 and y < minusY:
            minusY = y
    # print(plusX,minusX,plusY,minusY)
    all_x = plusX - minusX
    all_y = plusY - minusY
    print(abs(plusX - minusX) * abs(plusY - minusY))



