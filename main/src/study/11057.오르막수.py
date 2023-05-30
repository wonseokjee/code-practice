n = int(input())
k = [1]*10
for i in range(1,n):
    for j in range(1,10):
        k[j] += k[j-1]
print(sum(k)%10007)s
