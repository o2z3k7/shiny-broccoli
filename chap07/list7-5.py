# リストの全要素をenumerate関数で走査

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x,1):
    print('{}番目 = {}'.format(i,name))
    