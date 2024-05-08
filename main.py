from graphics import Window, Point, Line, Cell

if __name__ == "__main__":
  win = Window(800, 600)
  
  top_left = Point(100, 100)
  bottom_right = Point(350, 350)
  cell = Cell(win, has_bottom_wall = False, has_top_wall = False)

  cell.draw(top_left.x, top_left.y, bottom_right.x, bottom_right.y)

  win.wait_for_close()