from gameparts import Board
import pygame


pygame.init()

# Constants
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)


def draw_lines():
    """Draw the game grid."""

    # Draw horizontal lines.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Draw vertical lines.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_figures(board):
    """Draw X and O on the board."""

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(result: str) -> None:
    """Save the result of the game."""
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


def main():
    # Init the board.
    game = Board()
    draw_lines()

    current_player = 'X'
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get mouse position
                row = y // CELL_SIZE
                col = x // CELL_SIZE

                # Check if the cell is occupied. Make move if it's not.
                if game.board[row][col] != ' ':
                    continue
                game.make_move(row, col, current_player)

                # Check if the game is over
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
                draw_figures(game.board)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
