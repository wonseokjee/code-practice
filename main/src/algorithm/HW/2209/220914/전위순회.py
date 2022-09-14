def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


tc = int(input())
v = int(input())
arr = list(map(int, input().split()))
ch1 = [0] * (v+1)
ch2 = [0] * (v+1)
for i in range(v-1):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

print(f'#{tc}', end=' ')
preorder(1)