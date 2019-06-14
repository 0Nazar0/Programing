import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
a = input('Відпустка чи вихідний ')
if a == 'Відпустка' or a == 'Вихідний':
    print('Не включать будильник')
else:
    print('Включити будильник ')

printTimeStamp('Verbytskiy and Нескоромний Н. і Мальований')
    

