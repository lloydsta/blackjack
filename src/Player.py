
class Player():
    """
    Creates a Player object with an empty hand.
    """
    def __init__(self):
        self.player_hand = []

    def num_of_players(self):
        num_of_players = int(input("How many players? "))

