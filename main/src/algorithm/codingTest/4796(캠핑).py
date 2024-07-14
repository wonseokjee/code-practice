num = 0
while(True):
    L,P,V = list(map(int,input().split()))
    num += 1
    if(L == 0):
        break
    else:
        ins = V // P
        less = (V-P*ins)
        if less > L:
            less = L
        print(f"Case {num}: {L*ins + less}")
