def preorder(n):
    if 0<n <=N:
        print(chr(n+64), end='')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if 0< n <=N:
        inorder(ch1[n])
        print(chr(n+64), end='')
        inorder(ch2[n])

def postorder(n):
    if 0<n <=N:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n + 64), end='')

N = int(input())
ch1=[0]*(N+1)
ch2=[0]*(N+1)
#아스키코드  A=65
for i in range(1,N+1):
    x,a,b = map(str, input().split())
    if a != '.':
        ch1[ord(x)-64] = ord(a)-64 #아스키코드 변환 문자->숫자 ord 반대: chr
    if b != '.':
        ch2[ord(x)-64] = ord(b)-64

preorder(1)
print()
inorder(1)
print()
postorder(1)