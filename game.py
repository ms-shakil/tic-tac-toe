class TicTacToe:
    def __init_(self):
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
        move = [i for i,spot in enumerate(self.board) if spot == " "]
        return move
    
    def empty_squre(self):
        return " " in self.board

    def Num_empty_squre(self):
        return self.board.count(" ")    

    def make_moves(self,squre,letter):
        if self.board[squre] == " ":
            self.board[squre] = letter
            if self.winner(squre,letter):
                self.currentwinner = letter
            return True  
        return False      

    def winner(self):
        pass        
def Play(game,x_player,o_player,print_bord =True):
    if print_bord:
        game.printboard()
    letter = "X"
    while game.empty_squre():
        if letter == "O":
            squre = o_player.get_move(game)
        else:
            squre = x_player.get_move(game)    
        
        if game.make_move(squre,letter):
            if print_bord:
                print(letter + f"make a move to squre{squre}")
                game.printboard()
                print(" ")
            
            if game.currentwinner:
                if print_bord:
                    print(letter +"winner!")
            letter = "O" if letter == "X" else "X"    