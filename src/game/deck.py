from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        """
        Creating a deck,
        Then filling it with Cards
        """
        self.deck = []
        for i in range(14):
            for j in range(4):
                self.deck.append(Card(value=i, suit_no=j))

    def shuffle(self) -> list:
        """Just shuffle"""
        shuffle(self.deck)
        return self.deck

    def size(self) -> int:
        return len(self.deck)
