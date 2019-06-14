p = float(input('Тиск у паскалях: '))
v = float(input("Об'єм"))
r = 8.314
f = input('Цельсіях чи кельвін ')
t = float(input('Температура'))

if f == 'Цльсіях':
    a = t+273.15
    n = (p*v)/(r*a)
    print(n)
elif f == 'Кельвін':
    n = (p*v)/(r*t)
    print(n)

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний Н.,Вербитьськи, Мальваний')    
          
