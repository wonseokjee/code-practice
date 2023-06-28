arr = input()
sm_stack = []
lg_stack = []
sm_cal = 0
lg_cal = 0
ans = 0
for str in arr:
    if str == '(':
        sm_stack.append(str)
    elif str == ')':
        if len(sm_stack) != 0:
            sm_stack.pop()
            if len(sm_stack) == 0:
                sm_cal += 2

    if str == '[':
        lg_stack.append(str)
    elif str == ']':
        if len(lg_stack) != 0:
            lg_stack.pop()
print(len(sm_stack) + len(lg_stack))


