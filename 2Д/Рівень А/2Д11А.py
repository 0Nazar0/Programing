import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
import datetime, random

n = 1000
def first_kind_generator(n):
    for i in range(1, n + 1):
        p = random.randint(1, 6) + random.randint(1, 6)
        i += 1
        yield p
l = []
for i in first_kind_generator(n):
    l.append(i)
print("{:8}{:8}".format('Total','Simulated %'))
for i in range(2,13):
    print("{:2}{:12}".format(i, l.count(i)/10))
    i += 1


printTimeStamp("Нескоромний, Вербицький і Мальований")
