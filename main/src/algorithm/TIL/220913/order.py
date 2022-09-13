def preorder(n):#전위
    if n :
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): #중위순회
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


e = int(input())
arr = list(map(int, input().split()))
v = e + 1
root = 1
#부모를 인덱스로 자식 번호 저장
ch1 = [0]*(v+1)
ch2 = [0]*(v+1)
for i in range(e):
    p,c = arr[i*2], arr[i*2+1]
    if ch1[p]  == 0:
        ch1[p]  = c
    else:
        ch2[p] = c
preorder(root)

