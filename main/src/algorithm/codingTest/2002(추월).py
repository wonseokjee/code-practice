n = int(input())
inn = {i: input() for i in range(n)}
outt = {i: input() for i in range(n)}
inn_rev= {v:k for k,v in inn.items()}
visited = [False] * n
inn_cnt = 0
outt_cnt = 0
ans = 0
# print(inn)
# print(outt)
while(outt_cnt < n):
    if not visited[inn_cnt]:
        inn_num = inn.get(inn_cnt)
        outt_num = outt.get(outt_cnt)
        # print(inn_num,outt_num)
        if inn_num == outt_num:
            visited[inn_cnt] = True
            inn_cnt += 1
        else:
            visited[inn_rev.get(outt_num)] = True
            ans+=1
        outt_cnt += 1
    else:
        inn_cnt += 1
print(ans)
