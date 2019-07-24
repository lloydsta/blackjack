from Card import Card

class Deck():
    def __init__(self):
        self.case = []
        self._SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        self._RANK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        # Generate the deck (append each card to the "case" list)
        self.generate_deck()

    def generate_deck(self):
        for rank in self._RANK:
            for suit in self._SUITS:
                generated_card = Card(rank, suit)
                self.case.append(generated_card)
