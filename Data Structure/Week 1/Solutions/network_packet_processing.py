from collections import deque


def result(c, n):
    queue = deque()
    count = 0
    res = []
    for i in range(n):
        a, t = map(int, input().split())
        while queue and queue[0] <= a:
            queue.popleft()
            count -= 1
        if count >= c:
            res.append(-1)
        else:
            time = max(a, queue[-1]) if queue else a
            res.append(time)
            queue.append(time + t)
            count += 1
    return res


def main():
    c, n = map(int, input().split())
    res = result(c, n)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

# 3 5
# 0 3
# 0 4
# 0 2
# 9 2
# 10 3