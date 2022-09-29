n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    for j in range(i,n):
        if a[i] < b[j]:
            a[i],b[j] = b[j],a[i]
        else:
            break

print(sum(a))


# 5 3
# 1 2 5 4 3
# 5 5 6 6 5


