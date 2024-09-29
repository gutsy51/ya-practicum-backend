class Board:
    """Define the playing field with the ability to make move."""

    field_size: int = 3

    def __init__(self):
        """Initialize the board matrix where. Possible values are ' ', 'X', 'O'."""
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row: int, col: int, player: chr) -> None:
        """Process a player's turn.

        :param: row - row index.
        :param: col - column index.
        :param: player - 'X' or 'O'.
        """
        self.board[row][col] = player

    def display(self) -> None:
        """Print the board to the console."""
        width = self.field_size * 2 - 1
        for i, row in enumerate(self.board):
            print('|'.join(row))
            print('-' * width if i < len(self.board) - 1 else '')

    def is_board_full(self) -> bool:
        """Check if the board is full (it's a draw, game's over)."""
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_winner(self, player: chr) -> bool:
        """Check if the player has won the game."""
        # Check rows and columns.
        for i in range(self.field_size):
            if (
                all([self.board[i][j] == player for j in range(self.field_size)]) or
                all([self.board[j][i] == player for j in range(self.field_size)])
            ):
                return True

        # Check diagonals.
        if (
            all([self.board[i][i] == player for i in range(self.field_size)]) or
            all([self.board[i][-i-1] == player for i in range(self.field_size)])
        ):
            return True

        return False  # Not a winner.

    def __str__(self):
        """Print information about the board."""
        return (
            f'Board object with size of '
            f'{self.field_size}x{self.field_size}.'
        )
