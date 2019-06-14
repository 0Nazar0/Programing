a = input("Введіть букву: ")
if a == 'a' or a == 'e' or a =='i' or a == 'o' or a == 'u':
    
    print('Голосна')
elif a == "y":
    print('Голосна або Приголосна')
else:
    print('Приголосна')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Вербицький, Нескоромний, Мальований')    
          
