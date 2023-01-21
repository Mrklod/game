from random import choice
from PIL import Image

class Game:
    def __init__(self):
        print("""Всем знакомая игра""")
        value = ['камень','ножницы','бумага']
        ans = input("Выбирайте:(камень,ножницы или бумага)").lower()
        c = choice(value)
        if ans == 'камень' and c == 'камень':
            im = Image.open("img/nogniz.png")
            im.show()
            print('Ничья')
        elif ans == 'камень' and c == 'ножницы':
            print('Победа')
        elif ans == 'камень' and c == 'бумага':
            print('Поражение')
        if ans == 'ножницы' and c == 'ножницы':
            print('Ничья')
        elif ans == 'ножницы' and c == 'камень':
            print('Поражение')
        elif ans == 'ножницы' and c == 'бумага':
            print('Победа')
        if ans == 'бумага' and c == 'бумага':
            print('Ничья')
        elif ans == 'бумага' and c == 'ножницы':
            print('Поражение')
        elif ans == 'бумага' and c == 'камень':
            print('Победа')
        print(c)
