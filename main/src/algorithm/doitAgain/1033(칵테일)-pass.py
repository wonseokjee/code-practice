n = int(input())
arr = [list(map(int, input().split())) for _ in range(n-1)]
n_list = [1]*n
for a,b,p,q in arr:
    n_list[a] *= p/q
    n_list[b] *= q/p
print(n_list)