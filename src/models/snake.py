class Snake:
    """Модель змейки и управление её движением."""

    def __init__(self, start_position=(10, 10), initial_length=3):
        """Создаёт змейку заданной длины в начальной позиции."""
        self.start_position = start_position
        self.initial_length = initial_length
        self.reset()

    def reset(self):
        """Возвращает змейку в начальное состояние."""
        x, y = self.start_position

        self.body = [
            (x - i, y)
            for i in range(self.initial_length)
        ]

        self.direction = (1, 0)
        self.grow_pending = False

    def change_direction(self, new_direction):
        """Изменяет направление движения, запрещая разворот на 180 градусов."""
        dx, dy = self.direction
        new_dx, new_dy = new_direction

        if (dx + new_dx, dy + new_dy) == (0, 0):
            return

        self.direction = new_direction

    def move(self):
        """Перемещает змейку на одну клетку."""
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        """Увеличивает длину змейки на один сегмент."""
        self.grow_pending = True

    def get_head(self):
        """Возвращает координаты головы змейки."""
        return self.body[0]
