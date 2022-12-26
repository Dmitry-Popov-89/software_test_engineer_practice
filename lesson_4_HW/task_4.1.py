# Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
from decimal import Decimal

a = Decimal(input('Enter a real number: '))
b = input('Enter the required accuracy "0.0001": ')
dec_len = "0" * len(b.split('.')[1])
print(a.quantize(Decimal(f'1.{dec_len}')))
