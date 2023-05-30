a,b,c = map(int, input().split())

def dq(a,b,c):
    if b ==1:
        return a%c
    elif b%2==0:
        return (dq(a,b//2,c)**2)%c
    else:
        return ((dq(a,b//2,c)**2)*a)%c
print(dq(a,b,c))


