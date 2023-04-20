from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def start(self):
        while not self.board.is_game_over():
            self.print_board()
            row, col = self.get_move()
            self.board.make_move(row, col, self.current_player)
            self.current_player = "O" if self.current_player == "X" else "X"

        self.print_board()
        self.print_winner()

    def print_board(self):
        print(self.board)

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

    def print_winner(self):
        if self.board.is_winner("X"):
            print("X wins!")
        elif self.board.is_winner("O"):
            print("O wins!")
        else:
            print("It's a tie.")
