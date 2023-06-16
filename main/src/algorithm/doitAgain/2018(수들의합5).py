n = int(input())
ans = 1
cnt = 2
deg = 1
while n > deg:
    if cnt % 2 == 0:
        if n % cnt == cnt//2:
            ans += 1
    else:
        if n % cnt == 0:
            ans += 1
    deg += cnt
    cnt += 1
print(ans)