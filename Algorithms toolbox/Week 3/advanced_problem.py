from collections import deque, defaultdict

n = int(input())
nums = input().split()
d = defaultdict(deque)
for i in range(n):
    d[len(nums[i])].append(nums[i])
maximum = max(d.keys())

for i in range(maximum):
    d[i] = deque(sorted(d[i], reverse=True))

result = ''
f = '0'
while n:
    for i in range(1, maximum+1):
        # print(result)
        if d[i]:
            f = f if int(d[i][0][:len(f)]) <= int(f) else d[i][0]
    d[len(f)].popleft()
    result += f
    n -= 1
    f = '0'
print(result)
