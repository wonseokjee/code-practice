N = int(input())
five = N//5
cnt = -1
for i in range(five,-1,-1):
    if (N - (i*5)) % 2 == 0:
        cnt = i + ((N - (i*5)) // 2)
        break
print(cnt)