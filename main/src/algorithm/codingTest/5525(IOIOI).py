N = int(input())
M = int(input())
S = list(input())
O = 0
I = 0
cnt = 0
# 1부터 시작하는데 0이 O이면 카운트 X, I이면 카운트
if S[0] == 'I':
    I = 1
for i in range(1,len(S)):
    #O 이전에 I있으면 0 += 1
    # O 이전에 O이면 초기화
    if S[i] == 'O':
        if S[i-1] == 'I':
            O += 1
        else:
            O = 0
            I = 0
    else:
        # I이전에 O이거나 I ==0 이면 I+=1
        # I이전에 I이면 I = 1
        if S[i-1] == 'O' or I == 0:
            I += 1
        if S[i-1] == 'I':
            I = 1
            O = 0
    if O == N and I == N+1:
        cnt += 1
        O -= 1
        I -= 1
print(cnt)

# 2
# 25
# OOIOIIOIOIOIOIOIOIOIOOIOI

# 2
# 25
# OOIOIIOIOIOIOIOIOIOIOOIOI