t = 10
for i in range(1, t+1):
     print(*range(i, i*t+1, i), sep='\t')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний, Вербицький і Мальований')   
