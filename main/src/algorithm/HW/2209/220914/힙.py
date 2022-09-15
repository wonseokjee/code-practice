def heap_roof(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = last // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    last = 0
    heap = [0] * (N + 1)
    data = [0] + list(map(int, input().split()))

    for i in range(1, N + 1):
        heap_roof(data[i])

    result = 0
    t = last // 2

    while t:
        result += heap[t]
        t //= 2

    print(f'#{tc} {result}')