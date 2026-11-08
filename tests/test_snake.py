import unittest

from src.models.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(start_position=(10, 10), initial_length=3)

    def test_initial_position(self):
        self.assertEqual(
            self.snake.body,
            [(10, 10), (9, 10), (8, 10)]
        )

    def test_move(self):
        self.snake.move()

        self.assertEqual(self.snake.get_head(), (11, 10))
        self.assertEqual(len(self.snake.body), 3)

    def test_change_direction(self):
        self.snake.change_direction((0, 1))

        self.assertEqual(self.snake.direction, (0, 1))

    def test_reverse_direction_is_ignored(self):
        self.snake.change_direction((-1, 0))

        self.assertEqual(self.snake.direction, (1, 0))

    def test_grow(self):
        self.snake.grow()
        self.snake.move()

        self.assertEqual(len(self.snake.body), 4)

    def test_reset(self):
        self.snake.move()
        self.snake.reset()

        self.assertEqual(
            self.snake.body,
            [(10, 10), (9, 10), (8, 10)]
        )


if __name__ == "__main__":
    unittest.main()
