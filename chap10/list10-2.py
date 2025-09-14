"""min_max2モジュールのmin_max2関数を呼び出す"""

import list10_1
from chap10.list10_1 import min_max

x= float(input('実数x:'))
y= float(input('実数y:'))

mini,maxi= list10_1.min_max(x,y)
print('最小値は',mini,'です。')
print('最大値は',maxi,'です。')
