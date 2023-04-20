class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return "\n---------\n".join(" | ".join(row) + " |" for row in self.board)

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def is_game_over(self):
        return self.is_winner("X") or self.is_winner("O") or self.is_board_full()

    def is_board_full(self):
        return all(" " not in row for row in self.board)

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2-i] == player for i in range(3)):
            return True

        return False
