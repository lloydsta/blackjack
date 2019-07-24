from Deck import Deck
from Player import Player
from Dealer import Dealer
from Game import Game

# INITIALIZE
if __name__ == "__main__":
    # Create the game object
    my_game = Game()


def print_dealer_hand():
    print(my_game.dealer.dealer_hand)

def print_player_hand():
    print(my_game.player.player_hand)




print_dealer_hand()
print_player_hand()

#print(my_game.dealer_total)

my_game.apply_logic()