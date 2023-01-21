from cmn import Game


start = input("Играем?")
while start !='q' or start != 'quit':
    games = ['Камень ножницы бумага-1']
    for game in games:
        print(game)
    ans = int(input("""Дабы выбрать игру,необходимо нажать на номер,который соответствует номеру игры"""))
    if ans == 1:
        Game()
    start = input("Играем?")