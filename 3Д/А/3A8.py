
import datetime
rf = open("ФайлC.txt")
wf = open("ФайлB","w")
for string in rf:
    new_string = string.replace("\n","")
    wf.write(new_string)
    wf.write('. ')
rf.close()
wf.close()
printTimeStamp = lambda x: print('Автор програми: {0}\nЧас компіляції: {1}'.format(x, str(datetime.datetime.now())))
printTimeStamp("Нескоромний, Вербицький і Мальований")
