def dpChange(money: int, coins: list) -> int:
    """
    :param money: The amount to be changed
    :param coins: Array of coins
    :return: Minimum number of coins
    """
    DPlist = [0 for _ in range(money + 1)]
    for i in range(1, money + 1):
        minimum = money + 1
        for coin in coins:
            if i == coin:
                minimum = 0
                break
            if i >= coin and DPlist[i - coin] != 0:
                minimum = min(minimum, DPlist[i - coin])
        if minimum != money + 1:
            DPlist[i] = minimum + 1
        print(DPlist[i])
    return DPlist[-1]


money = 40
coins = [1, 5, 10, 20, 25]
print(dpChange(money, coins))
