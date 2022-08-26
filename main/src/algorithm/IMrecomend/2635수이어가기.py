N = int(input())
cnt_max = 0
arr_max= []
for a in range(1,N+1):
    cnt = 2
    x = N-a
    b = a
    arr = [N,b,x]
    while x >= 0:
        x, b = b-x, x
        arr.append(x)
        cnt+=1
    if cnt_max< cnt:
        cnt_max = cnt
        arr_max = arr
print(cnt_max)
print(*arr_max[:-1])
