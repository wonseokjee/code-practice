N = int(input())
cnt = 0
in_3 = [3,13,23,30,31,32,34,35,36,37,38,39,33,43,53]
#문자열 생각못하고 완전히 숫자로 접근...
for n in range(N+1):
    for m in range(60):
        for s in range(60):
            if n in in_3 or m in in_3 or s in in_3:
                cnt += 1
print(cnt)

# if '3' in str(n)+str(m)+str(s)
# 문자열 이용.