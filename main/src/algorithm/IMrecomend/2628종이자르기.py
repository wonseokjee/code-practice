width, height = map(int, input().split())
cut = int(input())
cut_width = []
cut_height = []
result_max = 0
result = 0

for _ in range(cut):
    direct, num = map(int, input().split())
    if direct == 0:
        cut_height.append(num)
    else:
        cut_width.append(num)
for i in range(len(cut_width)-1): #삽입정렬
    for j in range(i+1, len(cut_width)):
        if cut_width[i]< cut_width[j]:
            cut_width[i], cut_width[j] =  cut_width[j], cut_width[i]
for k in range(len(cut_height)-1): #삽입정렬
    for l in range(k+1, len(cut_height)):
        if cut_height[k] < cut_height[l]:
            cut_height[k] , cut_height[l] = cut_height[l],cut_height[k]
cut_width.append(0)
cut_height.append(0)
for a in range(len(cut_width)):
    if a == 0:
        range_width = width - cut_width[a]
    else:
        range_width =  cut_width[a-1] - cut_width[a]
    for b in range(len(cut_height)):
        if b == 0:
            range_height = height - cut_height[b]
        else:
            range_height = cut_height[b-1] - cut_height[b]
        result = range_height* range_width
        if result>result_max:
            result_max = result
print(result_max)