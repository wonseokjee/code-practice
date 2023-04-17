import itertools
N = int(input())
number = []
for i in range(1,N+1):
    number.append(i)

permutation = list(itertools.permutations(number))
# print(permutation)
# print(type(permutation[0]))
exam, *arg = map(int, input().split())
# print(exam, arg)
# print(tuple(arg))
if (exam == 1):
    ans = permutation[arg[0]-1]
    for i in ans:
        print(i,end=" ")
else:
    for j in range(len(permutation)):
        if (permutation[j] == tuple(arg)):
            print(j+1)




