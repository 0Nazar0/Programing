import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
flag = input("Вчом вимірювать? (inch, metr): ")
if flag == 'inch':
    d = float(input("Зріст: "))
    v = float(input("Маса: "))
    res = 700*(v/d**2)
    print(res)
elif flag == 'metr':
    d = float(input("Зріст: "))
    v = float(input("Маса: "))
    result = (v/d**2)
    print(result)   
printTimeStamp('Verbytskiy and Нескоромний Н. і Мальований')

