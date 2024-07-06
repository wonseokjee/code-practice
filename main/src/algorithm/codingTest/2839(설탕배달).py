N = int(input())
#5로 나누어짐 5,3으로 나누어짐, 안나누어짐, 3으로만 나누어짐
#5로 나누어질때
if N%5==0:
    print(N//5)
else:
    # 3을 빼면서 5로 나누어지는 판단
    m = 0
    while N > 0:
        m += 1
        N -= 3
        if N % 5 == 0:
            print(N//5 + m)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N==0:
            print(m)
            break

