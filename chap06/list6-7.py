#文字列txt内に文字列ptnは含まれているか

txt = input('文字列txt:')
ptn = input('文字列ptn:')

if ptn in txt:
    print('ptnはtxtに含まれています')
else:
    print('ptnはtxtに含まれていません')

