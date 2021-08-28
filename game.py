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

       

