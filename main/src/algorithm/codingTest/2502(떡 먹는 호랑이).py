d,k = map(int, input().split())

cnt = 2
sec, fir = 0,0
def dfs(k,i):
    global cnt, sec, fir
    l = k-i
    if l > 0 and i>l:
        cnt += 1
        # print(k,i,l)
        # print(cnt)
        if cnt != d:
            dfs(i,l)
        else:
            sec, fir = i, l

for i in range(k-1,k//2+1,-1):
    dfs(k,i)
    cnt = 2
    if sec > 0:
        print(fir)
        print(sec)
        break
# 2 26 28 54 82 136 218
