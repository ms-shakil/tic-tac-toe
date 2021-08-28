import math
import random

class Player:
    def __init__(self,letter):
        self.letter = letter

    def get_move (self,game) :
        pass

class RandomComPlayer(Player):
    def __init__(self,letter):
        super.__init__(self,letter)

    def get_move(self,game):
        squre = random.choice(game.available_move())
        return squre

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valide_squre = False
        val = None
        while not valide_squre:
            squre = input(self.letter + "input move (9-0):")
            try:
                val = int(squre)
                if val not in game.available_move():
                    raise ValueError
                valide_squre  = True
            except ValueError:
                print("invalid squre try again")     

        return val           

