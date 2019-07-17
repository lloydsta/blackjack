from Deck import Deck
from Player import Player
from Dealer import Dealer
from Game import Game

# INITIALIZE
if __name__ == "__main__":
    new_deck = Deck()
    dealer = Dealer(new_deck)
    player_one = Player()
    player_one.player_hand = dealer.deal()
    print(player_one.hand)




#
#
# #def deal_to_dealer():
# #    the_dealer.hand.append(current_deck._case.pop())
#
# def deal_to_player():
#     the_player.hand.append(current_deck._case.pop())



# """ FOR TESTING PURPOSES """
# print('Deck size = ' + str(len(current_deck._case)))
#
# deal_to_dealer()
# print(the_dealer.hand)
#
# deal_to_player()
# print(the_player.hand)
#
# print('Deck size = ' + str(len(current_deck._case)))
#
# deal_to_dealer()
# print(the_dealer.hand)
#
# deal_to_player()
# print(the_player.hand)
#
# print('Deck size = ' + str(len(current_deck._case)))


# Print each card in the deck
#print(current_deck._case)

# Print the size of the deck
#print('Deck size = ' + str(len(current_deck._case)))

# Deal the first card in the deck (list)
#current_deck._case.pop()