items, W = map(int, input().split())
bag = []
for _ in range(items):
    v, w = map(int, input().split())
    bag.append([v, w, v / w])

bag = sorted(bag, key=lambda x: -x[2])
n = 0
V = 0
while W > 0 and n < len(bag):
    V += bag[n][0] if bag[n][1] <= W else bag[n][0] * W / bag[n][1]
    W -= bag[n][1]
    n += 1
print(V)
