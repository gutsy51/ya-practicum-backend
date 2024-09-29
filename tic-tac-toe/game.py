from gameparts import Board
from gameparts.exceptions import *


def save_result(result: str) -> None:
    """Save the result of the game."""
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


def main():
    # Init the board.
    game = Board()
    print(game)
    current_player = 'X'
    is_running = True
    game.display()

    while is_running:
        print(f'< {current_player}\'s turn!')

        # Get coords from player with validation.
        while True:
            try:
                # Get coords.
                row = int(input('Enter the number of the row: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                col = int(input('Enter the number of the column: '))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError

                # Check if cell is occupied.
                if game.board[row][col] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    F'Values must be in the range from 0 to {game.field_size}.'
                )
                print('Please try again.')
            except ValueError:
                print('Value must be an integer. Please try again.')
            except CellOccupiedError:
                print('The cell is already occupied. Please try again.')
            except Exception as e:
                print(f'Unexpected error: {e}')
            else:
                break

        # All good. Make the move.
        game.make_move(row, col, current_player)
        game.display()

        # Check if the game is over.
        if game.is_winner(current_player) or game.is_board_full():
            if game.is_winner(current_player):
                result = f'{current_player} has won!'
            else:
                result = 'The game is a draw!'
            print(result)
            save_result(result)
            is_running = False

        # Next move.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
