from Deck import Deck
from Dealer import Dealer
from Player import Player

class Game():
    """
    Starts the game by initializing the dealer, player, and shuffled deck objects.
    Also handles all the logic.
    """

    def __init__(self):
        # Create the deck
        new_deck = Deck()

        # Create the dealer who shuffles the deck, create the player
        self.dealer = Dealer(new_deck)
        self.player = Player()

        # Deal cards to both dealer and player
        self.player.player_hand = self.dealer.initial_deal()

        # Calculate the totals of each player
        self.rank_total()

    def rank_total(self):
        self.dealer_total = self.dealer.dealer_hand[0]._Card__rank + self.dealer.dealer_hand[1]._Card__rank
        self.player_total = self.player.player_hand[0]._Card__rank + self.player.player_hand[1]._Card__rank
        return self.dealer_total, self.player_total

    def apply_logic(self):
        # Check for dealer blackjack
        #if self.dealer.dealer_hand[0]._Card__rank or self.dealer.dealer_hand[1]._Card__rank == 1:


        if self.dealer_total == 11 and self.player_total == 11:
            print('Push')
        elif self.dealer_total == 11 and self.player_total != 11:
            print('Dealer Blackjack, get fucked')
        elif self.dealer_total != 11 and self.player_total == 11:
            print('Blackjack, you win!')
        else:
            print('other')