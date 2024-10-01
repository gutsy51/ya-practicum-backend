from random import randint
from typing import Optional
import pygame


# Constants for field and grid sizes.
SCREEN_WIDTH, SCREEN_HEIGHT = 200, 200
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Directions.
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)  # Color of the board background.
BORDER_COLOR = (93, 216, 228)  # Color of the board border.
APPLE_COLOR = (255, 0, 0)  # Color of the apple.
SNAKE_COLOR = (0, 255, 0)  # Color of the snake.
SPEED = 10  # Speed of the snake.
WIN_SCORE = 20  # Score to win the game.

EVENT_PAUSE = 'Pause'
EVENT_EXIT = 'Exit'
EVENT_NONE = 'None'

# Set up the window.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('The Snake')

# Set up the clock.
clock = pygame.time.Clock()


class GameObject:
    """Abstract game object class"""

    _body_color = (1, 1, 1)

    def __init__(self,
                 position: tuple[int, int] = (0, 0),
                 body_color: tuple[int, int, int] = (1, 1, 1)) -> None:
        """Default values initialization."""
        self.position = position
        self.body_color = body_color

    def draw(self) -> None:
        """Abstract object rendering method."""
        raise NotImplementedError(
            'The GameObject.draw() method must be redefined in child class.'
        )


class Apple(GameObject):
    """Represent an Apple in the game."""

    def __init__(self) -> None:
        super().__init__(body_color=APPLE_COLOR)  # Init with red color.
        self.randomize_position()  # Set random position.
        self.draw()  # Show the apple.

    def draw(self) -> None:
        """Draw the apple on the game board."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def randomize_position(self) -> None:
        """Update `self.position` to a random position on the game board."""
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )


class Snake(GameObject):
    """Represent a Snake in the game"""

    def __init__(self) -> None:
        super().__init__(
            position=(
                GRID_WIDTH // 2 * GRID_SIZE,
                GRID_HEIGHT // 2 * GRID_SIZE
            ),
            body_color=SNAKE_COLOR
        )
        self.length: int = 1
        self.positions: list[tuple[int, int]] = [self.position]
        self.next_direction: Optional[tuple[int, int]] = None
        self.direction: tuple[int, int] = RIGHT

    @property
    def last(self):
        """Return the last position of the snake."""
        return self.positions[-1]

    def get_head_position(self):
        """Return the head position of the snake."""
        return self.positions[0]

    def __len__(self):
        """Return the size of the snake."""
        return self.length

    def set_next_direction(self, direction: tuple[int, int]) -> None:
        """Set the next direction of the snake."""
        self.next_direction = direction

    def draw(self) -> None:
        """Update the snake on the game board."""
        # Draw the body
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Remove the last segment
        if self.last != self.get_head_position():
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self):
        """Update `self.direction` based on `self.next_direction`."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Move the snake in the current direction."""
        # NewHead = (OldHead + SIZE*Direction) % screen
        # Modulo is used to avoid going out of the screen
        dx, dy = self.direction
        new_head: tuple[int, int] = (
            (self.positions[0][0] + dx * GRID_SIZE) % SCREEN_WIDTH,
            (self.positions[0][1] + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        self.update_direction()
        self.positions.insert(0, new_head)
        self.draw()
        self.positions.pop()

    def grow(self) -> None:
        """Add a new segment to the snake."""
        self.length += 1
        self.positions.append(self.last)
        self.move()

    def reset(self) -> None:
        """Reset the snake in case of game restart/snake crash."""
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT


def handle_keys(snake: Snake) -> str:
    """Return event type by key pressed."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Window closed. Exit the game.
            return EVENT_EXIT

        if event.type == pygame.KEYDOWN:
            # Button pressed. Update the direction.
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.set_next_direction(UP)
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.set_next_direction(DOWN)
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.set_next_direction(LEFT)
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.set_next_direction(RIGHT)

            # Escape pressed, pause the game.
            if event.key == pygame.K_ESCAPE:
                return EVENT_PAUSE
    return EVENT_NONE


def show_message(font: pygame.font.Font, text: str) -> None:
    """Creates a box with the specified text on the screen."""
    if not text:
        return

    renders = [
        font.render(line, True, (30, 30, 30)) for line in text.split('\n')
    ]

    mid = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    bg_rect_pos = (
        0, mid[1] - renders[0].get_height() // 2 - GRID_SIZE // 2
    )
    bg_rect_size = (
        SCREEN_WIDTH, renders[0].get_height() * len(renders) + GRID_SIZE
    )
    bg_rect = pygame.Rect(bg_rect_pos, bg_rect_size)
    pygame.draw.rect(screen, (230, 230, 230), bg_rect)

    for i, rendered in enumerate(renders):
        screen.blit(
            rendered,
            (mid[0] - rendered.get_width() // 2,
             mid[1] - (rendered.get_height() // 2) + rendered.get_height() * i)
        )


def redraw_window(snake: Snake, apple: Apple) -> None:
    """Redraw the game window."""
    screen.fill(BOARD_BACKGROUND_COLOR)
    snake.draw()
    apple.draw()


def main():
    """Main game loop."""
    # Init the game.
    pygame.init()
    font = pygame.font.Font(None, 20)
    is_paused: bool = True
    pause_msg: str = 'Press ESC to start the game!.'
    apple: Apple = Apple()
    snake: Snake = Snake()
    while apple.position == snake.get_head_position():
        # Avoid the apple on the snake.
        apple.randomize_position()
    apple.draw()
    snake.draw()

    pygame.display.update()
    while True:
        clock.tick(SPEED)

        event: str = handle_keys(snake)
        is_win: bool = len(snake) == WIN_SCORE
        is_lose: bool = snake.get_head_position() in snake.positions[1:]

        # Check if the game is over.
        if event == EVENT_EXIT:
            break

        # Check if the game is paused.
        elif is_paused:
            if event == EVENT_PAUSE:
                is_paused = False
                redraw_window(snake, apple)
            else:
                show_message(font, pause_msg)
        elif event == EVENT_PAUSE:
            is_paused = True
            pause_msg = 'The game is paused.\nESC to continue.'

        # Check if the snake eats the apple.
        elif snake.get_head_position() == apple.position:
            snake.grow()
            while apple.position in snake.positions:
                apple.randomize_position()
            apple.draw()

        # Check if the game is over.
        elif is_win or is_lose:
            pause_msg = (f'You {"won" if is_win else "lost"}!\n'
                         f'Score: {len(snake)}\nESC to restart.')
            snake.reset()
            is_paused = True

        # Move the snake.
        else:
            snake.move()

        # Update the screen.
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
