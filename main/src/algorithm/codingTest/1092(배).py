N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)
ans = 0
if box[0] > crane[0]:
    print(-1)
else:
    while len(box)>0:
        for i in crane:
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        ans += 1
    print(ans)
