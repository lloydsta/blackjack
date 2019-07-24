from Deck import Deck
import random

class Dealer():
    """
    Creates a Dealer object who takes in a deck and shuffles it.
    Also 'deals' the cards to himself and the player.
    """
    def __init__(self, deck):
        self.deck = deck.case
        self.shuffle_deck()
        self.dealer_hand = []

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def initial_deal(self):
        counter = 0
        player_holder = []
        while counter != 2:
            player_holder.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())
            counter += 1
        return player_holder
