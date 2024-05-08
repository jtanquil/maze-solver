from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height):
    self.__root = Tk()
    self.canvas = Canvas(self.__root, bg = "white", height = height, width = width)
    self.is_running = False
    
    self.__root.title("Maze Solver")
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
    self.canvas.pack(fill = BOTH, expand = 1)

  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self):
    self.is_running = True
    
    while self.is_running:
      self.redraw()

    print("Window closed...")

  def close(self):
    self.is_running = False

  def draw_line(self, line, fill_color = "black"):
    line.draw(self.canvas, fill_color)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, start_point, end_point):
    self.start_point = start_point
    self.end_point = end_point

  def draw(self, canvas, fill_color = "black"):
    canvas.create_line(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill = fill_color, width = 2)

class Cell:
  def __init__(self, win, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self._win = win

  def draw(self, x1, y1, x2, y2):
    if self.has_left_wall:
      left_wall = Line(Point(x1, y2), Point(x1, y1))
      self._win.draw_line(left_wall)
    
    if self.has_right_wall:
      right_wall = Line(Point(x2, y2), Point(x2, y1))
      self._win.draw_line(right_wall)

    if self.has_top_wall:
      top_wall = Line(Point(x1, y1), Point(x2, y1))
      self._win.draw_line(top_wall)

    if self.has_bottom_wall:
      bottom_wall = Line(Point(x1, y2), Point(x2, y2))
      self._win.draw_line(bottom_wall)