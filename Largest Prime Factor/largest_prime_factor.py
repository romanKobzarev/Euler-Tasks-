from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


a = 600_851_475_143
i = a
while i > 0:
    i -= 1
    if a % i == 0:
        if is_prime(i):
            print(i)
            break
