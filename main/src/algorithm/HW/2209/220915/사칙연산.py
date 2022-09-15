def postorder(n):
    if n <= N:
        if ch1[n]>0:
            postorder(ch1[n])
        if ch2[n] > 0:
            postorder(ch2[n])
        result.append(lst[n])



T = 10
for tc in range(1,T+1):
    N = int(input())
    lst = [0]
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(1, N+1):
        p, x, *ch = input().split()
        lst.append(x)
        if ch and ch1[i] == 0:
            ch1[i] = int(ch[0])
        if ch and ch1[i] != 0:
            ch2[i] = int(ch[1])
    result=[]
    postorder(1)
    # print(result)
    stack=[]
    for j in result:
        if j.isdigit():
            stack.append(int(j))
        else:
            a = stack.pop()
            b = stack.pop()
            if j =='+':
                stack.append(b+a)
            if j == '-':
                stack.append(b-a)
            if j == '/':
                stack.append(b/a)
            if j == '*':
                stack.append(b*a)

    print(f'#{tc}', end=' ')
    print("{:.0f}".format(stack[0]))


