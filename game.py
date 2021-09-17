import math
from player import HumanPlayer, RandomComPlayer 
class TicTacToe:
    def __init__(self):
        self.board =[" " for _ in range(9)]
        self.currentwinner = None
    
    def printboard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " |".join(row)+" |")
    @staticmethod
    def print_board_number():
        value = [[str(i)for i in range(j*3,(j+1)*3)]for j in range(3)]
        for i in value:
            print("| "+" |".join(i)+" |")

    def available_move(self):
        move = [i for i,x in enumerate(self.board) if x == " "]
        return move
    
    def empty_squre(self):
        return ' ' in self.board
   

    def Num_empty_squre(self):
        return self.board.count(' ')    

    def make_moves(self,squre,letter):
        if self.board[squre] == " ":
            self.board[squre] = letter
            if self.winner(squre,letter):
                self.currentwinner = letter
            return True  
        return False      

    def winner(self, square, letter):

        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False    
def Play(game,x_player,o_player,printgame =True):
    if printgame:
        game.print_board_number()
    letter = "X"
    while game.empty_squre():
        if letter == "O":
            squre = o_player.get_move(game)
        else:
            squre = x_player.get_move(game)    
        
        if game.make_moves(squre,letter):
            if printgame:
                print(letter + f"make a move to squre{squre}")
                game.printboard()
                print(" ")
            
            if game.currentwinner:
                if printgame:
                    print(letter +"winner!")

                return letter    
            letter = "O" if letter == "X" else "X"    
    if printgame:
        print("It's tie.")        

if __name__ == "__main__":
    x_p = HumanPlayer("X")
    o_p = RandomComPlayer("O")
    t = TicTacToe()
    Play(t,x_p, o_p, printgame = True)       