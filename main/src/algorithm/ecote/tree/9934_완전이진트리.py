#중위 순회 한게 입력으로 들어옴
def inorder(n):
    if n <= len(tree)-1:
        inorder(n*2)
        lst.append(n)
        inorder(n*2+1)



K = int(input())
tree = [0]+list(map(int, input().split()))
lst = [0]
result = []
inorder(1)
# print(tree, lst)

for i in range(1,len(lst)+1):
    for j in range(len(lst)):
        if i == lst[j]:
            result.append(tree[j])
            break
# print(result)
for i in range(1,K+1):
    if i == 1:
        print(result[0])
    else:
        for j in range(2**(i-1),2**i):
            print(result[j-1], end=' ')
        print()
