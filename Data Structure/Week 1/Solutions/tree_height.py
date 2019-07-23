from collections import deque


class node():
    def __init__(self, key):
        self.val = key
        self.child = []

    def addChild(self, child):
        self.child.append(child)


def createTree(n, keys):
    nodes = []
    for i in range(n):
        nodes.append(node(i))
    for i in range(n):
        key = keys[i]
        if key == -1:
            head = nodes[i]
        else:
            nodes[key].addChild(nodes[i])
    return head


def bfs(head):
    if not head.child:
        return 1
    queue = deque([[child, 2] for child in head.child])
    while queue:
        node1, level = queue.popleft()
        if node1.child:
            for child in node1.child:
                queue.append([child, level + 1])
    return level


def main():
    n = int(input())
    keys = list(map(int, input().split()))
    head = createTree(n, keys)
    level = bfs(head)
    print(level)


if __name__ == '__main__':
    main()

