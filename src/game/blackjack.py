from players import Player
from deck import Deck
from typing import List


class Blackjack:
    def __init__(self):
        self.players = List[Player(is_dealer=False)]
        self.dealer = Player(is_dealer=True)
        self.deck = Deck().shuffle()

    def deal(self):
        """
        Раздача карт.
        В начале игры раздается по 2 карты.
        """
        for _ in range(2):
            card = self.deck.pop(0)
            self.player.cards.append(card)
        for _ in range(2):
            card = self.deck.pop(0)
            self.dealer.cards.append(card)

    def hit(self, player: Player):
        player.hit(self.deck)
        player.show_cards()