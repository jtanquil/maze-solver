from graphics import Line, Point

class Cell:
  def __init__(self, win, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self._win = win

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    top_left = Point(self._x1, self._y1)
    top_right = Point(self._x2, self._y1)
    bottom_left = Point(self._x1, self._y2)
    bottom_right = Point(self._x2, self._y2)

    if self.has_left_wall:
      left_wall = Line(top_left, bottom_left)
      self._win.draw_line(left_wall)
    
    if self.has_right_wall:
      right_wall = Line(top_right, bottom_right)
      self._win.draw_line(right_wall)

    if self.has_top_wall:
      top_wall = Line(top_left, top_right)
      self._win.draw_line(top_wall)

    if self.has_bottom_wall:
      bottom_wall = Line(bottom_left, bottom_right)
      self._win.draw_line(bottom_wall)

  def get_x_midpoint(self):
    return self._x1 + abs(self._x2 - self._x1) // 2
  
  def get_y_midpoint(self):
    return self._y1 + abs(self._y2 - self._y1) // 2

  def draw_move(self, to_cell, undo = False):
    line_color = "gray" if undo else "red"
    self_x_midpoint = self.get_x_midpoint()
    self_y_midpoint = self.get_y_midpoint()
    other_x_midpoint = to_cell.get_x_midpoint()
    other_y_midpoint = to_cell.get_y_midpoint()
    move_line = Line(Point(self_x_midpoint, self_y_midpoint), Point(other_x_midpoint, other_y_midpoint))

    print(f"drawing line from ({self_x_midpoint}, {self_y_midpoint}) to ({other_x_midpoint}, {other_y_midpoint})")
    self._win.draw_line(move_line, line_color)
