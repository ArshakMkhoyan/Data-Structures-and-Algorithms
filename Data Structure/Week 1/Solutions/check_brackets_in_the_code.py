def index(br):
    if br in '([{':
        return '([{'.index(br)
    else:
        return ')]}'.index(br)


def isSuccess(brackets):
    opening = '([{'
    i = 0
    stack = []
    while i < len(brackets):
        if brackets[i] in '([{}])':
            bracket = brackets[i]
            if bracket in opening:
                stack.append((bracket, i))
            else:
                if not stack:
                    return i + 1
                last, id = stack.pop()
                if (index(last) == index(bracket)) and (last != bracket):
                    pass
                else:
                    return i + 1
        i += 1

    if not stack:
        return 'Success'
    else:
        last, id = stack.pop()
        return id + 1


def main():
    brackets = input()
    ans = isSuccess(brackets)
    print(ans)


if __name__ == '__main__':
    main()
