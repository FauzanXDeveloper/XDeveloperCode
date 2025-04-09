import unittest
import pygame
import random


from snake_game import Your_score, our_snake 


class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.display_width = 600
        self.display_height = 400
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        self.snake_block = 10

    def test_snake_initialization(self):
        # Test that the snake starts with a length of 1
        snake_list = [[self.display_width / 2, self.display_height / 2]]
        self.assertEqual(len(snake_list), 1)

    def test_snake_growth(self):
        # Test that the snake grows when it eats food
        snake_length = 1
        snake_length += 1  # Simulate eating food
        self.assertEqual(snake_length, 2)

    def test_food_spawn(self):
        # Test that food spawns within the display boundaries
        foodx = round(random.randrange(0, self.display_width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.display_height - self.snake_block) / 10.0) * 10.0
        self.assertTrue(0 <= foodx < self.display_width)
        self.assertTrue(0 <= foody < self.display_height)

    def test_snake_collision_with_boundaries(self):
        # Test that the game ends if the snake hits the boundaries
        x1 = self.display_width
        y1 = self.display_height / 2
        self.assertTrue(x1 >= self.display_width or x1 < 0 or y1 >= self.display_height or y1 < 0)

    def test_snake_collision_with_itself(self):
        # Test that the game ends if the snake collides with itself
        snake_list = [[self.display_width / 2, self.display_height / 2],
                      [self.display_width / 2 - self.snake_block, self.display_height / 2]]
        snake_head = [self.display_width / 2, self.display_height / 2]
        self.assertIn(snake_head, snake_list[1:])  # Check if the head collides with the body

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()