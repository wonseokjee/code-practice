n = list(input())
answer = -1
n_sort = sorted(n,reverse=True)
n_int = list(map(int, n))
sum_n = sum(n_int)
# print(n_int, sum_n)
if 0 in n_int and sum_n % 3 == 0:
    answer = ''.join(n_sort)
print(answer)
