def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
import datetime

print("число в кПа: ")
a = float(input())

print ("фт/дм2: ", a*0.145038)

 
printTimeStamp("Нескоромний. Вербицький і Мальований")
