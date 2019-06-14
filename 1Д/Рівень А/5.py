a = int(input('Введіть любу цифру '))
F = int(a * 9/5 + 32)
K = int(a + 273.15)
print(a, 'Цельсій')
print(F, 'Фаренгейт')
print(K, 'Келвін')
import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Вербицький,Нескоромний,Мальований')

