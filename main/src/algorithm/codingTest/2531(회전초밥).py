import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())

cp1, cp2 = 0, k-1
arr = []
for _ in range(N):
    arr.append(int(input()))
check = set()

while cp1 < N:
    if cp2 >= N:
        cp2 -= N
    if cp2 < cp1:
        plates = arr[cp1:] + arr[:cp2+1]
    else:
        plates = arr[cp1:cp2+1]
    plates_continue = set(plates)
    if c not in plates_continue:
        plates_continue.add(c)
    if len(check) < len(plates_continue):
        check = plates_continue
    cp1 += 1
    cp2 += 1
print(len(check))
