import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = list(input("Enter: "))
if len(a) < 6:
    print("ERROR
          ")
else:
    for i in range(3):
        del a[a.index(max(a))]
        del a[a.index(min(a))]
    print("A =", a)



printTimeStamp("Нескоромний,Вербицький і Мальований")

