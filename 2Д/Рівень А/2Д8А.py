import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
import random, itertools, datetime
def satolloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  
        items[j], items[i] = items[i], items[j]
    print("\nsatollo\n", items)

cards = []
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck = list(itertools.product(vals, suits))
for val, suit in deck:
    cards.append('%s of %s' % (val, suit))

print("original\n", cards)
satolloCycle(cards)
printTimeStamp("Нескоромний, Вербицький і Мальований")
