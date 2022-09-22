T = int(input())
for tc in range(1,T+1):
    con, truck = map(int, input().split())
    con_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))
    con_lst.sort(reverse=True)
    truck_lst.sort(reverse=True)
    print(con_lst,truck_lst)
    cnt = 0
    for i in range(len(truck)):
        j = 0
        for j in range(len(con)):
            if truck_lst[i] > con_lst[j]:
                cnt += con_lst[j]
                k = j
                break