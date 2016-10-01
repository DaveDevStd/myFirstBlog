import gry, random

print('Witaj w prostej grze\n')

again = None
while again != 'n':
    players = []
    num = gry.askNumber(question = 'Podaj liczbe graczy (2 - 5): ',low = 2, high = 5)

    for i in range(num):
        name = input('Nazwa gracza: ')
        score = random.randrange(100) + 1
        player = gry.Player(name, score)
        players.append(player)

    print('\nOto wyniki gry:')
    for player in players:
        print(player)

    again = gry.askYesNo('\nCzy chcesz zagrac ponownie? (t/n): ')

    input('Enter')

