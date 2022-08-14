T = int(input())
for tc in range(1,T+1):
    n = input()
    stick = 1
    piece = 0
    for i in range(1,len(n)):
        if n[i] == '(':
            stick +=1
        else:
            stick -=1
            if n[i-1] == '(':
                piece += stick
            else:
                piece += 1
    print(f'#{tc} {piece}')
