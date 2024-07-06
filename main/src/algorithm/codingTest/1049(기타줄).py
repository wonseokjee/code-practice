N,M = map(int,input().split())
package = 1001
separate = 1001
ans = 0
for t in range(M):
    pack, sep = map(int,input().split())
    if package > pack:
        package = pack
    if separate > sep:
        separate = sep
if separate * 6 < package:
    ans = separate * N
else:
    ans += (N // 6) * package
    if (N % 6)*separate >= package:
        ans += package
    else:
        ans += (N % 6) * separate
print(ans)