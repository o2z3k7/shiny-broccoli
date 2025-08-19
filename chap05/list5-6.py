# 算術演算用の組み込み関数の利用例
import math

x = float(input('実数x:'))
y = float(input('実数y:'))
z = float(input('実数z:'))

print('abs(x)=', abs(x))
print('bool(x)=', bool(x))
print('divmod(x,y)=', divmod(x,y))
print('max(x, y)=', max(x, y))
print('min(x, y)=', min(x, y))
print('pow(x,y)=', pow(x,y))
print('round(x,2)=', round(x,2))
print('round(x,3)=', round(x,3))
print('sum(x,y,z)=',sum((x,y,z)))
