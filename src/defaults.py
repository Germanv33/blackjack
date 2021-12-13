from collections import namedtuple


Suit = namedtuple('Suit', ['name', 'icon'])

HEART_ICON = '♥'
DIAMOND_ICON = '♦'
CLUB_ICON = '♦'
SPADE_ICON = '♠'

SUITS = {
    0: Suit('Hearts', HEART_ICON),
    1: Suit('Diamonds', DIAMOND_ICON),
    2: Suit('Clubs', CLUB_ICON),
    3: Suit('Spades', SPADE_ICON)
}

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
