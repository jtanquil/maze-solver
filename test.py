import unittest
import random

from maze import Maze

class TestMaze(unittest.TestCase):
  def setUp(self):
    self.num_rows = random.randint(1, 10)
    self.num_cols = random.randint(1, 10)
    self.x_coord = random.randint(0, 100)
    self.y_coord = random.randint(0, 100)
    self.x_size = random.randint(10, 100)
    self.y_size = random.randint(10, 100)

    self.maze = Maze(self.x_coord, self.y_coord, self.num_rows, self.num_cols, self.x_size, self.y_size)

  def test_maze_create_cells(self):
    self.assertEqual(len(self.maze._cells), self.num_cols)
    
    for i in range(self.num_cols):
      self.assertEqual(len(self.maze._cells[i]), self.num_rows)
      
      for j in range(self.num_rows):
        expected_top_left_x = self.x_coord + self.x_size * i
        expected_top_left_y = self.y_coord + self.y_size * j
        expected_bottom_right_x = expected_top_left_x + self.x_size
        expected_bottom_right_y = expected_top_left_y + self.y_size

        test_cell = self.maze._cells[i][j]
        self.assertEqual(test_cell._x1, expected_top_left_x)
        self.assertEqual(test_cell._y1, expected_top_left_y)
        self.assertEqual(test_cell._x2, expected_bottom_right_x)
        self.assertEqual(test_cell._y2, expected_bottom_right_y)

  def test_maze_break_entrance_and_exit(self):
    self.maze._break_entrance_and_exit()
    
    self.assertFalse(self.maze._cells[0][0].has_top_wall)
    self.assertFalse(self.maze._cells[-1][-1].has_bottom_wall)

if __name__ == "__main__":
  unittest.main()