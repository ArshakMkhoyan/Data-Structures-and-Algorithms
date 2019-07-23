def siftDown(n):
    id = n
    if array[id] > array[2 * n + 1]:
        id = 2 * n + 1
    if 2 * n + 2 < l and array[id] > array[2 * n + 2]:
        id = 2 * n + 2
    if id != n:
        array[n], array[id] = array[id], array[n]
        res.append([n, id])
        if id <= l // 2 - 1:
            siftDown(id)


def main():
    for i in range(l // 2 - 1, -1, -1):
        siftDown(i)


if __name__ == '__main__':
    l = int(input())
    array = list(map(int, input().split()))
    res = []
    main()
    print(len(res))
    for i in res:
        print(*i)

# 4
# 5 4 3 2
# 5
# 1 2 3 4 5
