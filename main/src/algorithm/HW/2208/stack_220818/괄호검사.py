T = int(input())
for tc in range(1, T+1):
    text = input()
    save_text = []
    boolen_text = 1
    for i in text:
        if i == '{' or i == '(':
            save_text.append(i)

        if i == '}'or i ==')':
            if save_text ==[]:
                boolen_text = 0
                break
            else:
                if i =='}':
                    if save_text[-1] == '{':
                        save_text.pop()
                    else:
                        boolen_text = 0
                        break
                if i == ')':
                    if save_text[-1] == '(':
                        save_text.pop()
                    else:
                        boolen_text = 0
                        break
    if save_text != []:
        boolen_text = 0
    print(f'#{tc} {boolen_text}')

