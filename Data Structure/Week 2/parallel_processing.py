def siftDown(n, threads):
    id = n
    if 2 * n + 2 < t and threads[2 * n + 2][1] == threads[2 * n + 1][1]:
        id = 2 * n + 1 if threads[2 * n + 1][0] < threads[2 * n + 2][0] else 2 * n + 2
    else:
        if threads[id][1] >= threads[2 * n + 1][1]:
            id = 2 * n + 1
        if 2 * n + 2 < t and threads[id][1] > threads[2 * n + 2][1]:
            id = 2 * n + 2
    if id != n:
        threads[id], threads[n] = threads[n], threads[id]
        if id <= t // 2 - 1:
            siftDown(id)


# def main():
#     for job in jobs:
#         res.append(threads[0])
#         threads[0][1] += job
#         siftDown(0)


if __name__ == '__main__':
    t, l = map(int, input().split())
    jobs = list(map(int, input().split()))
    threads = [[i, 0] for i in range(t)]
    res = []
    for job in jobs:
        # res.append(threads[0].copy())
        print(*threads[0])
        threads[0][1] += job
        siftDown(0, threads)
    # print(res)

# Tests

# 2 5
# 1 2 3 4 5

# 4 20
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
