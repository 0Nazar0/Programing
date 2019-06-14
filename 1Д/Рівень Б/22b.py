a = float(input(('Частота радіації ')))
if a < (3 * 10**9):
    print('Radio waves')
elif (3 * 10**9) < a < (3 * 10**12):
    print('microwaves')
elif (3 * 10**12) < a < (4.3 * 10**14):
    print('Infrared light')
elif (4.3 * 10**14) < a < (7.5 * 10**14):
    print('Visible light')   
elif (7.5 * 10**14) < a < (3 * 10**17):
    print('Utlaviolet light')
elif (3 * 10**17) < a < (3 * 10**19):
    print('X-rays')
elif (3 * 10**19) < a:
    print('Gamma rays')
    
    
import datetime    
def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Нескоромний,Вербицький і Мальований')
