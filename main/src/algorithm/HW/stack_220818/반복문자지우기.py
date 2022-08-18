T = int(input())
for tc in range(1,T+1):
    text = input()
    len_text = len(text)
    arr = []
    cnt = 0
    for i in range(0, len_text):
        if arr == []:
            arr.append(text[i])
            continue
        if arr[-1] == text[i]:
            arr.pop()
        else:
            arr.append(text[i])
    print(f'#{tc} {len(arr)}')



