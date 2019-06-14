import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
def GCD(x,y):
    if x == y:
        return x
    if x > y:
        return GCD(x-y, y)
    else:
        return GCD(x, y-x)
print(GCD(26,5))

printTimeStamp = lambda x: print('Автор програми: {0}\nЧас компіляції: {1}'.format(x, str(datetime.datetime.now())))
printTimeStamp("Нескоромний, Вербицький і Мальований")
