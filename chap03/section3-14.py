# aはbで割り切れるか

a = int(input('整数a:'))
b = int(input('整数b:'))

#bが0でなければaをbで割った剰余
c = b != 0 and a % b # bが0でなければaをbで割った剰余
print(c, end='・・・')

if c :
    print('aはbで割り切れません。')
else:
    print('bが0またはaがbで割り切れます。')
