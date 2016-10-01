class Player(object):
    """Uczestnik gry"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep

def askYesNo(question):
    """Zadaj pytanie na ktore mozna odpowiedziec tak lub nie"""
    response = None
    while response not in ('t', 'n'):
        response = input(question).lower()
    return response

def askNumber(question, low, high):
    """Popros o podanie liczby z okreslonego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == '__main__':
    print('Uruchomoles ten modul bezposrednio (zamiast go importowac)')
    input('Enter')
