#読み込んだ文字列内から文字をタンsカウ
s = input('文字列s:')
c = input('探す文字c:')

print('文字{}は'.format(c), end =' ')

for i in range(len(s)):
    if s[i] == c:
        print('s[{}]に入っています。'.format(i))
        break
else:
    print('入っていません。')