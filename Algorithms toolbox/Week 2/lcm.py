def gcd(a, b):
    while a != 0 and b != 0:
        a, b = b, a % b
    return max(a, b)


def lcm(a, b):
    print(a * b // gcd(a, b))


a, b = map(int, input().split())
lcm(a, b)