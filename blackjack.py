#Blackjack

import karty, gry

class BJCard(karty.Card):
    """Karta do blackjacka"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFaceUp:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJDeck(karty.Deck):
    """Talia do blackjacka"""
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))

class BJHand(karty.Hand):
    """Reka w blackjacku"""
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + '\t' + super(BJHand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

    @property
    def total(self):
        # jesli karta w rece ma wartosc None, to i wartosc sumy wunosi None
        for card in self.cards:
            if not card.value:
                return None
        #zsumuj wartosci kart, traktuj kazdego asa jako 1
        t = 0
        for card in self.cards:
            t += card.value

        #ustal czy reka zawiera asa
        containsAce = False

        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                containsAce = True
        #jesli reka zawiera asa, a suma jest niska
        #potraktuj asa jako 11
        if containsAce and t <= 11:
            #dodaj tylko 10, poniewsz dodalismy 1 za asa
            t += 10
        return t

    def isBusted(self):
        return self.total > 21

class BJPlayer(BJHand):
    """Gracz w blackjacku"""
    def isHitting(self):
        response = gry.askYesNo('\n' + self.name + ', chcesz dobrac karte? (t/n): ')
        return response == 't'
    
    def bust(self):
        print(self.name, 'ma fure.')
        self.lose()
        
    def lose(self):
        print(self.name, 'przegrywa')

    def win(self):
        print(self.name, 'wygrywa')

    def push(self):
        print(self.name, 'remisuje')

class BJDealer(BJHand):
    """Rozdajacy w blackjacku"""
    def isHitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, 'ma fure')

    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class BJGame(object):
    """Gra w blackjacka"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)
            
        self.dealer = BJDealer('Rozdajacy')

        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp

    def __additionalCards(self, player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player])
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        #rozdaj kazdemu po 2 karty
        self.deck.deal(self.player + [self.dealer], perHand = 2)
        self.dealer.flipFirstCard() # ukryj pierwsza karte rozdajacego
        for player in self.players:
            print(player)
        print(self.dealer)

        #rozdaj graczom dodatkowe karty
        for player in self.player:
            self.__additionalCards(player)

        self.dealer.flipFirstCard() #odslon pierwsza karte rozdajacego

        if not self.stillPlaying:
            #poniewaz wszyscy gracze dostali fure, pokaz tylko reke rozdajacego
            print(self.dealer)
        else:
            # daj dodatkowe karty rozdajacemu
            print(self.dealer)
            self.__additionalCards(self.dealer)

        if self.dealer.isBusted():
            #wygrywa kazdy kto jeszcze pozostaje w grze
            for player in self.stillPlaying:
                player.win()
        else:
            #porownaj punkty graczy z punktami rozdajacego
            for player in self.stillPlaying:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total() < self.dealer.total:
                    player.lose()
                else:
                    player.push()
        #usun karty wszystkich graczy
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print('\t\tWitaj w grze Blackjack\n')

    names = []
    number = gry.askNumber('Podaj liczbe graczy (1 - 7): ', low = 1, high = 8)
    for i in range(number):
        name = input('Wprowadz nazwe gracza: ')
        names.append(name)
    print()

    game = BJGame(names)

    again = None
    while again != 'n':
        game.play()
        again = gry.askYesNo('\nCzy chcesz zagrac ponownie? (t/n): ')

main()
input('Enter')
