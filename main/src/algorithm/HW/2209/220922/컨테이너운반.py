T = int(input())
for tc in range(1,T+1):
    con, truck = map(int, input().split())
    con_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))
    con_lst.sort()
    truck_lst.sort()
    # print(con_lst,truck_lst)
    cnt = 0
    while(truck_lst and con_lst):
            if truck_lst[-1] >= con_lst[-1]:
                cnt += con_lst.pop()
                truck_lst.pop()
            else:
                con_lst.pop()
    print(f'#{tc} {cnt}')

