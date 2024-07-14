lst = list(input())
cnt_X = 0
cnt_dot = 0
ans = ''
for x in lst:
    if x == 'X':
        cnt_X += 1
        if cnt_dot > 0:
            ans += '.' * cnt_dot
            cnt_dot = 0
    else:
        cnt_dot += 1
        if cnt_X > 0:
            ans += 'AAAA'*(cnt_X // 4)
            if cnt_X % 4 not in [0,2]:
                ans = -1
                cnt_X = 0
                cnt_dot = 0
                break
            ans += 'B'*(cnt_X % 4)
            cnt_X = 0
if cnt_X > 0:
    ans += 'AAAA'*(cnt_X // 4)
    ans += 'B'*(cnt_X % 4)
    if cnt_X % 4 not in [0,2]:
        ans = -1
    cnt_X = 0
if cnt_dot > 0:
    ans += '.' * cnt_dot
    cnt_dot = 0
print(ans)