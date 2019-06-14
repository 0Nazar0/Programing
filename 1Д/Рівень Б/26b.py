n = int(input('Введіть значення(2 або більше): '))
factor = 2
if n > 2:
    while factor <= n:
        if n%2 != 0:
            f = factor%n
            print(f)
        else:
            l=factor+1
            print(l%n)
else:
    print("Помилка ви маєте вести 2 або більше")
    
import datetime    
def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний, Вербицький і Мальований')
