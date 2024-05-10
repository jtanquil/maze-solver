import unittest
import random

from maze import Maze

class TestMaze(unittest.TestCase):
  def test_maze(self):
    for n in range(10):
      num_rows = random.randint(1, 10)
      num_cols = random.randint(1, 10)
      maze = Maze(0, 0, num_rows, num_cols, 100, 100)

      print(f"testing maze with num_rows = {num_rows}, num_cols = {num_cols}")
      self.assertEqual(len(maze._cells), num_cols)
      
      for j in range(num_cols):
        self.assertEqual(len(maze._cells[j]), num_rows)

if __name__ == "__main__":
  unittest.main()