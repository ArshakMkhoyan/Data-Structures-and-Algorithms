def gcd(a, b):
    while a != 0 and b != 0:
        a, b = b, a % b
    print(max(a, b))


a, b = map(int, input().split())
gcd(a, b)
