import random


def toss_coin():
    return random.choice([True, False])


def calc(money, win):
    if win:
        return money * 0.5
    else:
        return money * 1.8


def test():
    money = 100
    for i in range(100):
        money = calc(money, toss_coin())
        # print('times: %s, result: %s, money: %.2f, ' % (i + 1, win, money))
    return money


win_times, lose_times = 0, 0
max_money, min_money = 100, 100
for times in range(10000):
    cur_money = test()
    if cur_money > 100:
        win_times += 1
        max_money = max(max_money, cur_money)
    else:
        lose_times += 1
        min_money = min(min_money, cur_money)

print('win: %s, lose: %s' % (win_times, lose_times))
print('max_money: %.2f, min_money: %.2f' % (max_money, min_money))
