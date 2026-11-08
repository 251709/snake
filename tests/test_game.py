import unittest

from src.models.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(5, 5)

    def test_initial_state(self):
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.game_over)
        self.assertEqual(len(self.game.snake.body), 3)

    def test_move(self):
        initial_head = self.game.snake.get_head()

        self.game.update()

        self.assertEqual(
            self.game.snake.get_head(),
            (initial_head[0] + 1, initial_head[1])
        )

    def test_eat_food(self):
        head_x, head_y = self.game.snake.get_head()
        self.game.food.position = (head_x + 1, head_y)

        self.game.update()

        self.assertEqual(self.game.score, 1)
        self.assertEqual(len(self.game.snake.body), 4)

    def test_wall_collision(self):
        for _ in range(3):
            self.game.update()

        self.assertTrue(self.game.game_over)

    def test_reset(self):
        self.game.score = 5
        self.game.game_over = True

        self.game.reset()

        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.game_over)
        self.assertEqual(len(self.game.snake.body), 3)

    def test_game_does_not_update_after_game_over(self):
        self.game.game_over = True
        initial_body = self.game.snake.body.copy()

        self.game.update()

        self.assertEqual(self.game.snake.body, initial_body)


if __name__ == "__main__":
    unittest.main()
