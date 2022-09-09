food_times = list(map(int, input().split()))
k = int(input())
len_food = len(food_times)
sum_food = sum(food_times)
# print(sum_food)
a = 0
i = 1
# for i in range(1, sum_food+1):
#     l = i % len_food
#     if l == 0:
#         l = len_food
#     if food_times[l-1] == 0:
#         a += 1
#         continue
#     food_times[l-1] -= 1
def roof(sum_food, i ,a):
    global food_times
    j = i
    roof_a = a
    for b in range(j, sum_food+1+a):
        l = b % len_food
        if l == 0:
            l = len_food
        if food_times[l-1] == 0:
            sum_food += 1
            roof_a += 1
            continue
        if b - roof_a - 1 == k:
            print(l)
            break
        food_times[l-1] -= 1
        j += 1

    roof(sum_food+roof_a, j, a)
roof(sum_food,i, a)


