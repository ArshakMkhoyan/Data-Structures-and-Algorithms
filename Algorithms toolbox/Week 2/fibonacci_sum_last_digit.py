def last_d(n):
    n %= 60
    if n < 2:
        print(n)
    a, b = 0, 1
    digit = 1
    for i in range(2, n+1):
        a, b = b, (a+b) % 10
        digit = (digit + b) % 10
    print(digit)


n = int(input())
last_d(n)