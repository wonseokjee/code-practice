N = list(map(int, input()))
if len(N)%2 ==0:
    len_N = len(N)//2
    if sum(N[:len_N]) == sum(N[len_N:]):
        print('LUCKY')
    else:
        print('READY')
