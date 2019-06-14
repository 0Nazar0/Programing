from random import randint
import time
print("Введіть гравця")
name=input()
print(name + "кидає кубик")
time.sleep(3)
n1=randint(1,6)
print('Випало n1')
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Verbytskiy and Neskoromnuy і Мальований')
