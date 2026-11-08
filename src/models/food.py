import random


class Food:
    """Модель еды, появляющейся на игровом поле."""

    def __init__(self, field_width, field_height):
        """Создаёт еду для поля заданного размера."""
        self.field_width = field_width
        self.field_height = field_height
        self.position = None

    def spawn(self, occupied_cells):
        """Размещает еду в случайной свободной клетке."""
        free_cells = [
            (x, y)
            for x in range(self.field_width)
            for y in range(self.field_height)
            if (x, y) not in occupied_cells
        ]

        if not free_cells:
            self.position = None
            return

        self.position = random.choice(free_cells)

    def get_position(self):
        """Возвращает координаты еды."""
        return self.position
