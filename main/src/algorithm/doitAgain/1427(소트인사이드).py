import sys
input = sys.stdin.readline
arr = list(map(str, input()))
arr.sort(reverse=True)
arr.pop()
print(''.join(arr))
