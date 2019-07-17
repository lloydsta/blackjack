
class Card():
    """Defines a single card including its rank and suit"""

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def print_card(self):
        print('Rank is {}'.format(self.__rank))
        print('Suit is {}'.format(self.__suit))

    def __repr__(self):
        return str(self.__rank) + ' of ' + str(self.__suit)