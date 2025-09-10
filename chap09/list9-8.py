# 暗算トレーニング（３桁の整数を三つ加える）

import random

def confirm_retry():
    """もう一度行うかどうかを確認する"""
    while True:
        n = int(input('もう一度？<Yes・・・1/No・・・0>：'))
        if n == 0 or n == 1:
            return n

print('暗算トレーニング開始！')

while True:
    x = random.randint(100,900)
    y = random.randint(100, 900)
    z = random.randint(100, 900)

    while True:
        print(x,'+',y,'+',z,'=',end=' ')
        k = int(input())
        if k == x + y + z:
            break
        print('違いますよ！！')

    if not confirm_retry():
        break

