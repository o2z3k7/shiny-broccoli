# 読み込んだ整数値以下の全約数を列挙

n = int(input('整数値：'))

for i in range(1, n+1):
    if n % i == 0:
        print(i, end = ' ')
print()

# nをiで割った剰余が0であれば（nがiで割り切れれば）、iはnの約数となるため、その値を表示する
