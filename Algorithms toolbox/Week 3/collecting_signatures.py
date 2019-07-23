n = int(input())
build = []
for i in range(n):
    build.append(list(map(int, input().split())))
build = sorted(build, key=lambda x: x[0])
print(build)
result = []
i = 0
while i < n:
    bound = build[i][1]
    i += 1
    while i < n and build[i][0] <= bound:
        bound = min(bound, build[i][1])
        i += 1
    result.append(bound)
print(len(result))
print(*result)
