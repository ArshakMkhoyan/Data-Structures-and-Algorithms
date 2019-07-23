class dissets:
    def __init__(self, maximum, ds, rows):
        self.maximum = maximum
        self.ds = ds
        self.rows = rows

    def find(self, i):
        if i != self.ds[i]:
            self.ds[i] = self.find(self.ds[i])
        return self.ds[i]

    def union(self, j, k):
        a = self.find(j)
        b = self.find(k)
        if a != b:
            self.rows[a] += self.rows[b]
            self.maximum = max(self.maximum, self.rows[a])
            self.ds[b] = a


if __name__ == '__main__':
    n, m = map(int, input().split())
    rows = list(map(int, input().split()))
    maximum = max(rows)
    ds = [i for i in range(n)]
    paths = []
    for i in range(m):
        paths.append(list(map(int, input().split())))

    obj = dissets(maximum, ds, rows)
    for path in paths:
        j, k = path
        obj.union(j - 1, k - 1)
        print(obj.maximum)

# 5 5
# 1 1 1 1 1
# 3 5
# 2 4
# 1 4
# 5 4
# 5 3

# 6 4
# 10 0 5 0 3 3
# 6 6
# 6 5
# 5 4
# 4 3

