ans = [1,3]
for i in range(2, 30):
    case = ans[i-1] + 2*ans[i-2]
    ans.append(case)
T = int(input())
for tc in range(1, T+1):
    cnt = int(input()) // 10
    print(f'#{tc} {ans[cnt -1]}')
