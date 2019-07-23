def last_d(n):
    n %= 60
    if n < 2:
        return max(0, n)
    a, b = 0, 1
    digit = 1
    for i in range(2, n+1):
        a, b = b, (a+b) % 10
        digit = (digit + b) % 10
    return digit


m, n = map(int, input().split())

print((10 - last_d(m-1) + last_d(n)) % 10)
