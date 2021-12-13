from src import defaults


class Card:
    """
    suit_no
    0 - HEART_ICON = '♥'
    1 - DIAMOND_ICON = '♦'
    2 - CLUB_ICON = '♦'
    3 - SPADE_ICON = '♠'
    """
    def __init__(self, value: int, suit_no: int):
        assert suit_no in defaults.SUITS.keys(), 'Choose valid number from 0 to 3'
        self.cost = value
        self.value = defaults.VALUES[value - 1]
        self.suit = defaults.SUITS[suit_no]

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit.icon}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')

    def get_price(self) -> int:
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost
