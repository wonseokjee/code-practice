N = int(input())
dice = list(map(int, input().split()))
close_face = [[0,1,2],[0,1,3],[0,3,4],[0,2,4],[5,1,2],[5,1,3],[5,4,3],[5,4,2]]
n = N-2
##인접한 면 8가지중 최소값 찾고
##해당하는 변수에 대입
min = 151
min_num = []
for i in range(8):
    x,y,z = close_face[i]
    if min > dice[x]+dice[y]+dice[z]:
        min_num = [dice[x], dice[y], dice[z]]
        min = dice[x]+dice[y]+dice[z]

min_num.sort()
A = min_num[0]
AB = min_num[0] + min_num[1]
ABC = min_num[0] + min_num[1] + min_num[2]
# print(min, min_num)

ans = ABC*4 + AB*n*8 + AB*4 + A*n*4 + A*(n**2)*5
if N ==1:
    srt_dice = list(sorted(dice))
    print(sum(srt_dice[:-1]))
else:
    print(ans)

    # 6
    # 3 6 26 45 10 17

