import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input("Введи цифру для постройки піраміди: "))
def generate_lis(n):
    r = []
    for i in range(n):
        len_lis = len(r)
        r = [1 if i == 0 or i == len_lis else r[i-1]+r[i] for i in range(len_lis+1)]
        yield r
def print_pyramid(n):
    pyr = list(generate_lis(n))
    max = len('   '.join(map(str, pyr[-1])))
    for i in pyr:
        print('   '.join(map(str, i)).center(max)+'\n')
print_pyramid(n)

printTimeStamp("Нескоромний, Верббицький і Мальований")
