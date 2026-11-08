import unittest

from src.models.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food(10, 10)

    def test_spawn(self):
        occupied = [(0, 0), (1, 0), (2, 0)]

        self.food.spawn(occupied)

        self.assertIsNotNone(self.food.position)
        self.assertNotIn(self.food.position, occupied)

    def test_food_inside_field(self):
        self.food.spawn([])

        x, y = self.food.get_position()

        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 10)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, 10)

    def test_spawn_when_no_free_cells(self):
        occupied = [(x, y) for x in range(10) for y in range(10)]

        self.food.spawn(occupied)

        self.assertIsNone(self.food.position)

    def test_get_position(self):
        self.food.spawn([])

        self.assertEqual(self.food.get_position(), self.food.position)


if __name__ == "__main__":
    unittest.main()
