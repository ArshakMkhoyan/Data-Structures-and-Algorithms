from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
d = defaultdict(int)
for i in nums:
    d[i] += 1
    if d[i] > len(nums)//2:
        print(1)
        break
else: print(0)
