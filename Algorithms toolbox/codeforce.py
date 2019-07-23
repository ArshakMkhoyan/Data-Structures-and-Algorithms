from collections import deque, defaultdict

n, m = map(int, input().split())
d = defaultdict(deque)
for line in range(m):
    frm, to = map(int, input().split())
    d[frm].append(to)
    d[to].append(frm)
visited = set()
visitedinloop = set()
queue = deque()
final = 0
for i in range(1, n + 1):
    if i not in visited:
        toadd = True
        visited.add(i)
        queue += d[i]
        toadd = (len(d[i]) == 2 and toadd)
        visitedinloop.add(i)
        while queue:
            tocheck = queue.popleft()
            if tocheck not in visitedinloop:
                visited.add(tocheck)
                visitedinloop.add(tocheck)
                queue += d[tocheck]
                toadd = ((len(d[tocheck]) == 2) and toadd)
        final += toadd
print(final)
