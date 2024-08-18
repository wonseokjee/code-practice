k = int(input())
order = []
length = []
cnt = [0,0,0,0]
for i in range(6):
    x,y = map(int,input().split())
    order.append(x)
    length.append(y)
    cnt[x-1] += y
max_cnt = max(cnt)
min_cnt = min(cnt)
order_1 = length.index(max_cnt)
order_2 = length.index(min_cnt)
def find_num(num):
    if num == 0:
        return abs(length[1] - length[-1])
    elif num == 5:
        return abs(length[0]-length[4])
    else:
        return abs(length[num-1] - length[num+1])
print(((max_cnt*min_cnt)-(find_num(order_2)*find_num(order_1)))*k)



