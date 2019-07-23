def fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def fib_big(n):
    n = n % 60
    print(fib(n) % 10)


n = int(input())
fib_big(n)
