import pygame

from src.models.game import Game
from src.ui.renderer import Renderer


class SnakeApp:
    """Главное приложение игры Змейка."""

    CELL_SIZE = 30
    FIELD_WIDTH = 20
    FIELD_HEIGHT = 20
    FPS = 10

    def __init__(self):
        """Инициализирует игровое окно и компоненты игры."""
        pygame.init()

        self.screen = pygame.display.set_mode((
            self.FIELD_WIDTH * self.CELL_SIZE,
            self.FIELD_HEIGHT * self.CELL_SIZE
        ))

        pygame.display.set_caption("Snake")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)

        self.game = Game(
            field_width=self.FIELD_WIDTH,
            field_height=self.FIELD_HEIGHT
        )

        self.renderer = Renderer(
            self.screen,
            cell_size=self.CELL_SIZE
        )

        self.running = True

    def handle_events(self):
        """Обрабатывает события клавиатуры и окна."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                directions = {
                    pygame.K_UP: (0, -1),
                    pygame.K_DOWN: (0, 1),
                    pygame.K_LEFT: (-1, 0),
                    pygame.K_RIGHT: (1, 0)
                }

                if event.key in directions:
                    self.game.change_direction(directions[event.key])

    def draw_game_over(self):
        """Отображает сообщение о завершении игры."""
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        text = self.font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2
            )
        )

        self.screen.blit(text, text_rect)

    def run(self):
        """Запускает основной игровой цикл."""
        while self.running:
            self.handle_events()

            self.game.update()

            self.renderer.draw(self.game)

            if self.game.game_over:
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
