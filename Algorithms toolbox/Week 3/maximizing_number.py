n = int(input())
res = []
i = 1
while 2*i < n:
    res.append(i)
    n -= i
    i += 1
res.append(n)
print(len(res))
print(*res)
