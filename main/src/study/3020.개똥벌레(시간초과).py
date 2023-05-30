n,h = map(int, input().split())
obstacle = [int(input()) for _ in range(n)]
# print(n,h,obstacle)
section = [0]*h
# print(section)
cnt = 0
for i in range(1,n+1):
    if i%2==1:
        for j in range(obstacle[i-1]):
            section[j] += 1
    else:
        for k in range(h-1,(h-1)-obstacle[i-1],-1):
            section[k] += 1
# print(section)
obstacle_min = min(section)
obstacle_min_cnt = section.count(obstacle_min)
print(obstacle_min,obstacle_min_cnt)



