
import pygame


class Renderer:
    """Отвечает за отображение игровых объектов на экране."""

    BACKGROUND_COLOR = (25, 25, 25)
    GRID_COLOR = (40, 40, 40)
    SNAKE_COLOR = (50, 200, 80)
    HEAD_COLOR = (30, 240, 100)
    FOOD_COLOR = (230, 60, 60)
    TEXT_COLOR = (255, 255, 255)

    def __init__(self, screen, cell_size=30):
        """Создаёт отрисовщик для игрового окна."""
        self.screen = screen
        self.cell_size = cell_size
        self.font = pygame.font.Font(None, 32)

    def draw_grid(self, field_width, field_height):
        """Отрисовывает сетку игрового поля."""
        for x in range(field_width + 1):
            position_x = x * self.cell_size

            pygame.draw.line(
                self.screen,
                self.GRID_COLOR,
                (position_x, 0),
                (position_x, field_height * self.cell_size)
            )

        for y in range(field_height + 1):
            position_y = y * self.cell_size

            pygame.draw.line(
                self.screen,
                self.GRID_COLOR,
                (0, position_y),
                (field_width * self.cell_size, position_y)
            )

    def draw_snake(self, snake):
        """Отрисовывает все сегменты змейки."""
        for index, (x, y) in enumerate(snake.body):
            color = self.HEAD_COLOR if index == 0 else self.SNAKE_COLOR

            rect = pygame.Rect(
                x * self.cell_size,
                y * self.cell_size,
                self.cell_size,
                self.cell_size
            )

            pygame.draw.rect(
                self.screen,
                color,
                rect,
                border_radius=5
            )

    def draw_food(self, food):
        """Отрисовывает еду."""
        position = food.get_position()

        if position is None:
            return

        x, y = position

        center = (
            x * self.cell_size + self.cell_size // 2,
            y * self.cell_size + self.cell_size // 2
        )

        pygame.draw.circle(
            self.screen,
            self.FOOD_COLOR,
            center,
            self.cell_size // 2 - 3
        )

    def draw_score(self, score):
        """Отображает количество набранных очков."""
        text = self.font.render(
            f"Score: {score}",
            True,
            self.TEXT_COLOR
        )

        self.screen.blit(text, (10, 10))

    def draw(self, game):
        """Отрисовывает текущее состояние игры."""
        self.screen.fill(self.BACKGROUND_COLOR)

        self.draw_grid(game.field_width, game.field_height)
        self.draw_snake(game.snake)
        self.draw_food(game.food)
        self.draw_score(game.score)
