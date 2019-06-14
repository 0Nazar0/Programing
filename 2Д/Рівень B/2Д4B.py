import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
import datetime, math

n = int(input("Input n: "))
a = [i for i in range(n + 1)]
for i in range(2, int(math.ceil(math.sqrt(n)))):
    if a[i] != 0:
        j = i*i
        while j < n:
            a[j] = 0
            j = j + i
a = set(a[2:-1])
a.remove(0)
print(*a)


printTimeStamp("Нескоромний, Вербицьки і Мальований")
