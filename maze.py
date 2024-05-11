import time, random

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
    win = None
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

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)

    self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
    self._draw_cell(self.num_cols - 1, self.num_rows - 1)

  def _break_walls_r(self, i, j):
    current_cell = self._cells[i][j]
    current_cell.visited = True

    while True:
      to_visit = []

      for increment in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
          adjacent_cell = self._cells[i + increment[0]][j + increment[1]]
          if not adjacent_cell.visited:
            to_visit.append(adjacent_cell)
        except IndexError:
          continue

      if len(to_visit) == 0:
        self._draw_cell(i, j)
        return
      else:
        chosen_cell = to_visit[random.randrange(len(to_visit))]
        new_i, new_j = i, j

        if current_cell._x1 == chosen_cell._x1 and current_cell._y1 == chosen_cell._y2:
          current_cell.has_top_wall = False
          chosen_cell.has_bottom_wall = False
          
          new_j -= 1
        elif current_cell._x2 == chosen_cell._x1 and current_cell._y1 == chosen_cell._y1:
          current_cell.has_right_wall = False
          chosen_cell.has_left_wall = False
          
          new_i += 1
        elif current_cell._x1 == chosen_cell._x1 and current_cell._y2 == chosen_cell._y1:
          current_cell.has_bottom_wall = False
          chosen_cell.has_top_wall= False
          
          new_j += 1
        elif current_cell._x1 == chosen_cell._x2 and current_cell._y1 == chosen_cell._y1:
          current_cell.has_left_wall = False
          chosen_cell.has_right_wall = False

          new_i -= 1
        else:
          return
        
        self._draw_cell(i, j)
        self._break_walls_r(new_i, new_j)


  def _animate(self):
    self.win.redraw()
    time.sleep(0.005)