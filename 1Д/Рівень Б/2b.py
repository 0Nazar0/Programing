import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
a = input("Введіть місце проживання:")
b = input("Введіть час проведення дома:")
if a == 'Будинок' and int(b) >=18:
	print("В'этнамське Порося")
elif a == 'Будинок' and int(b) >=10<17:
	print('Собака')
elif a == 'Будинок' and int(b) <=10:
        print('Змія')
elif a == 'Квартира' and int(b) >=10:
        print('Кішка')
elif a == 'Квартира' and int(b) <=10:
        print('Хомяк')
elif a == 'Гуртожиток' and int(b) >=6:
        print('Рибки')
elif a == 'Гуртожиток' and int(b) <=6:
        print('Мурашник')

printTimeStamp('Verbytskiy and Нескоромний Н.і Мальований')
