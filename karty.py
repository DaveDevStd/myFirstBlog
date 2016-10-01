# Gra w karty 

class Card(object):
    """Karta do gry"""
    RANKS = ['A','2','3','4','5','6','7',
	     '8','9','10','J','Q','K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit, faceUp = True):
        self.rank = rank
        self.suit = suit
        self.isFaceUp = faceUp

    def __str__(self):
        if self.isFaceUp:
            rep = self.rank + self.suit
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.isFaceUp = not self.isFaceUp

class Hand(object):
    """Reka - karty do gry w reku gracza"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '<pusta>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    """Talia do gry"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, perHand = 1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard, hand)
                else:
                    print('Nie moge rozdawac. Brak kart')

if __name__ == '__main__':
    print('To modul zawierajacy klasy do gry w karty.')
    input('Enter')




