import math


def is_palindrome(k):
    n = str(k)
    if n == n[::-1]:
        return True
    return False


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
while(True):
    if n ==1:
        n = 2
    if is_palindrome(n):
        if is_prime(n):
            print(n)
            break
    n += 1
