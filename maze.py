import time

from cell import Cell

class Maze:
  def __init__(
    self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win
  ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self._cells = []

    self._create_cells()

  def _create_cells(self):
    for i in range(self.num_cols):
      self._cells.append([Cell(self.win) for j in range(self.num_rows)])

    for i in range(len(self._cells)):
      for j in range(len(self._cells[i])):
        self._draw_cell(i, j)

  def _draw_cell(self, i, j):
    top_left_x = self.x1 + self.cell_size_x * i
    top_left_y = self.y1 + self.cell_size_y * j
    bottom_right_x = top_left_x + self.cell_size_x
    bottom_right_y = top_left_y + self.cell_size_y

    self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)

    self._animate()

  def _animate(self):
    self.win.redraw()
    time.sleep(0.05)