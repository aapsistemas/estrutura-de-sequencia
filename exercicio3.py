import math
n = int(input('digite um numero de tres digitos'))
rev = 0

while n > 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)
