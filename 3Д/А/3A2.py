import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
import datetime
def catalan(n):
    if n == 0:
        return 1
    else:
        return catalan(n-1)*2*(2*n-1)//(n+1)
print(catalan(17))
printTimeStamp("Нескоромний, Вербицький і Мальований")
