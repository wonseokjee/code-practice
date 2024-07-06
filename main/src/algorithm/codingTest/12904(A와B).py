S = input()
T = input()
ans = 0
lst = list(T)
while(len(S) < len(lst)):
    if lst[-1] == 'A':
        lst.pop()
    else:
        lst.pop()
        lst = list(reversed(lst))
# print(lst)
if lst == list(S):
    ans = 1
print(ans)


