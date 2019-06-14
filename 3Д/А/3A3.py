import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)
print(power(9,12))
printTimeStamp("Нескоромний,Мальований і Вербицький")
