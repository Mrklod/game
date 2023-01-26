from random import choice
from PIL import Image

class Game:
    def __init__(self):
        print("""Всем знакомая игра""")
        value = ['камень','ножницы','бумага']
        ans = input("Выбирайте:(камень,ножницы или бумага)").lower()
        c = choice(value)
        if ans == 'камень' and c == 'камень':
            im = Image.open("img/camen.jpg")
            im.show()
            print('Ничья')
        elif ans == 'камень' and c == 'ножницы':
            im = Image.open("img/nogniz.jpg")
            im.show()
            print('Победа')
        elif ans == 'камень' and c == 'бумага':
            im = Image.open("img/paper.jpg")
            im.show()
            print('Поражение')
        if ans == 'ножницы' and c == 'ножницы':
            im = Image.open("img/nogniz.jpg")
            im.show()
            print('Ничья')
        elif ans == 'ножницы' and c == 'камень':
            im = Image.open("img/camen.jpg")
            im.show()
            print('Поражение')
        elif ans == 'ножницы' and c == 'бумага':
            im = Image.open("img/paper.jpg")
            im.show()
            print('Победа')
        if ans == 'бумага' and c == 'бумага':
            im = Image.open("img/paper.jpg")
            im.show()
            print('Ничья')
        elif ans == 'бумага' and c == 'ножницы':
            im = Image.open("img/nogniz.jpg")
            im.show()
            print('Поражение')
        elif ans == 'бумага' and c == 'камень':
            im = Image.open("img/camen.jpg")
            im.show()
            print('Победа')
        print(f'Противник показал: {c}')
