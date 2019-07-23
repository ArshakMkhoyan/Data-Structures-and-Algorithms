n = int(input())

l = [0] * (n + 1)

for k in range(1, n):
    i = k + 1
    if i % 2 == 0 and i % 3 == 0:
        l[i] = min(l[i // 2], l[i // 3], l[i - 1]) + 1
    elif i % 2 == 0:
        l[i] = min(l[i // 2], l[i - 1]) + 1
    elif i % 3 == 0:
        l[i] = min(l[i // 3], l[i - 1]) + 1
    else:
        l[i] = l[i - 1] + 1

print(l[-1])

result = []
m = l[-1]
while n != 1:
    result.append(n)
    m -= 1
    if n % 3 == 0 and l[n // 3] == m:
        n //= 3
    elif n % 2 == 0 and l[n // 2] == m:
        n //= 2
    else:
        n -= 1
result.append(1)
print(*result[::-1])

### Recursive

# n = int(input())
#
# T = {}
#
# def calc(i):
#     if i not in T:
#         if i == 1:
#             T[i] = 0
#         elif i % 2 == 0 and i % 3 == 0:
#             T[i] = min(calc(i//2), calc(i//3), calc(i - 1)) + 1
#         elif i % 2 == 0:
#             T[i] = min(calc(i // 2), calc(i - 1)) + 1
#         elif i % 3 == 0:
#             T[i] = min(calc(i // 3), calc(i - 1)) + 1
#         else:
#             T[i] = calc(i - 1) + 1
#     return T[i]
# print(calc(n))