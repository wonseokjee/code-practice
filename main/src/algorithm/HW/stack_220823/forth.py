T = int(input())
for tc in range(1, T+1):
    N = input().split()
    stack = []
    cnt = 'error'

    def add(b,c):
        num = b+c
        return num
    def substract(b,c):
        num = b-c
        return num
    def multiply(b,c):
        num = b*c
        return num
    def divide(b,c):
        num = b//c
        return num

    def cal(a,b,c):
        int_value = 0
        if a == '+':
            int_value = add(b,c)
        elif a == '-':
            int_value = substract(b,c)
        elif a == '/':
            int_value = divide(b,c)
        elif a == '*':
            int_value = multiply(b,c)
        return int_value

    for i in N:

        if i.isdigit():
            stack.append(int(i))
        else :
            if len(stack) > 1:
                int2 = stack.pop()
                int1 = stack.pop()
                num = cal(i,int1,int2)
                stack.append(num)
            else :
                if i == '.':
                    cnt = stack.pop()
                else:
                    break

    print(f'#{tc} {cnt}')
