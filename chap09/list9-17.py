# 2個以上の任意の個数の値の最大値を求める

def max2more(a,b,*num):
    """2個以上の任意の個数の値の最大値を求める"""
    max = a if a>b else b
    for n in num:
        if n > max:
            max = n
    return max

print('max2more(1,2)=',max2more(1,2))
print('max2more(1,2,3)=',max2more(1,2,3))

print('max2more(1,2,3,4,5)=',max2more(1,2,3,4,5))
### print('max2more(1)=',max2more(1))

