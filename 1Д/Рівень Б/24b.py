a = float(input('Введіть уровень шуму в децибелах:' ))
if a > 130:
    print('більше ніж jackhammer')
elif a == 130:
    print('jackhammer')
elif 130>a>106:
    print('между jackhammer і gas lawnmower ')
elif a == 106:
    print('gas lawnmower')
elif 106 > a > 70:
    print('между gas lawnmowe і alarm clock')
elif a == 70:
    print('alarm clock')
elif 70 > a > 40:
    print('между alarm clock і quiet room')
elif a == 40:
    print('quiet room')
elif a < 40:
    print('менше ніж quiet room ')
    
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний,Вербицький і Мальований')
