def find_cycle(m):
    result = [0, 1, 1]
    n = 3
    while not (result[-2] == 0 and result[-1] == 1):
        result.append((result[-2] + result[-1]) % m)
    return len(result) - 2


def fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def fib_huge(n , m):
    cycle = find_cycle(m)
    n = n % cycle
    print(fib(n) % m)


n, m = map(int, input().split())
fib_huge(n , m)
