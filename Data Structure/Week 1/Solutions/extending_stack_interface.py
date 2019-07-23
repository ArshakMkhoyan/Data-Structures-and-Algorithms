class maxStack:
    def __init__(self):
        self.stack = []
        self.max = []
        self.res = []

    def Push(self, val):
        self.max.append(max(val, self.max[-1]) if self.max else val)
        self.stack.append(val)

    def Pop(self):
        self.stack.pop() if self.stack else None
        self.max.pop() if self.max else None

    def Max(self):
        self.res.append(self.max[-1] if self.max else None)


def rules(obj, com, val):
    if com == 'push':
        obj.Push(int(val[0]))
    elif com == 'pop':
        obj.Pop()
    else:
        obj.Max()


def main():
    n = int(input())
    obj = maxStack()
    for _ in range(n):
        com, *val = input().split()
        rules(obj, com, val)
    print(*obj.res, sep='\n')


if __name__ == '__main__':
    main()
# 11
# push 5
# push 4
# push 8
# push 2
# push 10
# max
# pop
# max
# pop
# pop
# max