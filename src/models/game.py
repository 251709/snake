from src.models.snake import Snake
from src.models.food import Food
from src.models.highscore import HighScore


class Game:
    """Управляет игровой логикой змейки."""

    def __init__(self, field_width=20, field_height=20):
        """Создаёт новую игру с заданными размерами поля."""
        self.field_width = field_width
        self.field_height = field_height

        self.high_score_storage = HighScore()
        self.high_score = self.high_score_storage.load()

        self.reset()

    def reset(self):
        """Перезапускает игру и сбрасывает счёт."""
        start_position = (
            self.field_width // 2,
            self.field_height // 2
        )

        self.snake = Snake(
            start_position=start_position,
            initial_length=3
        )

        self.food = Food(self.field_width, self.field_height)
        self.food.spawn(self.snake.body)

        self.score = 0
        self.game_over = False

    def change_direction(self, direction):
        """Передаёт змейке новое направление движения."""
        if not self.game_over:
            self.snake.change_direction(direction)

    def check_collision(self):
        """Проверяет столкновения со стенами и телом змейки."""
        head_x, head_y = self.snake.get_head()

        # Проверка выхода за границы поля.
        if (
            head_x < 0
            or head_x >= self.field_width
            or head_y < 0
            or head_y >= self.field_height
        ):
            return True

        # Проверка столкновения головы с собственным телом.
        if self.snake.get_head() in self.snake.body[1:]:
            return True

        return False

    def update(self):
        """Обновляет состояние игры на один игровой шаг."""
        if self.game_over:
            return

        head_x, head_y = self.snake.get_head()
        dx, dy = self.snake.direction

        next_head = (head_x + dx, head_y + dy)

        # Проверяем, попадёт ли змейка на еду.
        if next_head == self.food.get_position():
            self.snake.grow()

        self.snake.move()

        if self.check_collision():
            self.game_over = True
            return

        # Начисляем очки и размещаем новую еду.
        if self.snake.get_head() == self.food.get_position():
            self.score += 1
            self.high_score = self.high_score_storage.update(self.score)
            self.food.spawn(self.snake.body)
