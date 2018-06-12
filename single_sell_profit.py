#!/usr/bin/python3.6

def buy_sell(A):
    if len(A) < 2:
        return 0
    mid = len(A) // 2
    buy_days = A[:mid]
    sell_days = A[mid:]
    return max([max(sell_days) - min(buy_days), 0])


def buy_sell_full(A):
    if len(A) < 2:
        return 0
    mid = len(A) // 2
    left_profit = buy_sell_full(A[:mid])
    right_profit = buy_sell_full(A[mid:])
    full_profit = buy_sell(A)
    return max([left_profit, right_profit, full_profit, 0])

if __name__ == '__main__':
    tests = [
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [420, 420, 69, 420],
        [69, 420, 420, 42069],
        [1, 3],
        [1, 2, 3],
        [69, 0, 69, 420],
        [0, 420, -69, 69]
    ]
    for test in tests:
        print(test, buy_sell_full(test))
