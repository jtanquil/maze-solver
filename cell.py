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
      bottom_wall = Line(bottom_left, bottom_rights)
      self._win.draw_line(bottom_wall)