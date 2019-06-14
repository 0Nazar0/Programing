import math
a = float(input('Введіть любу цифру '))
S = math.pi*a**2
v = 4/3*math.pi*a**3
print(a, 'radius')
print(S, 'площа')
print(v, 'обєм')
import datetime

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний, Вербицький і Мальований')
