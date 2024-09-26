N = int(input())
array = [0]*10000
for i in range(N):
    k = int(input())
    array[i] = k
d = [0]*10000
d[0] = array[0]
d[1] = array[0]+array[1]
d[2] = max(array[2]+d[0],d[1],array[1]+array[2])
for j in range(3,N):
    d[j] = max(array[j]+array[j-1]+d[j-3], array[j]+d[j-2], d[j-1])
print(max(d))