

class Player:
    def __init__(self, is_dealer: bool):
        self.cards = []
        self.score = 0
        self.is_dealer = is_dealer

    def check_score(self) -> int:
        ace_counter = 0
        self.score = 0
        for card in self.cards:
            if card.cost() == 11:
                ace_counter += 1
            self.score += card.cost()

        while ace_counter != 0 and self.score > 21:
            ace_counter -= 1
            self.score -= 10
        return self.score

    def hit(self, deck):
        """
        Добавление карты из общей колоды в колоду игрока

        Эта функция используется в классе BlackJack
        """
        self.cards.append(deck.cards.pop(0))

    def show_cards(self):
        if not self.is_dealer:
            print('Your cards:')
            for card in self.cards:
                card.show()
            print(f'Score: {self.score}')
        else:
            print('Dealer cards:')
            for card in self.cards:
                card.show()
            print(f'Dealer score: {self.score}')
