from graphics import Window, Point
from cell import Cell

if __name__ == "__main__":
  win = Window(800, 600)
  
  top_left = Point(100, 100)
  bottom_right = Point(300, 300)
  cell = Cell(win, has_right_wall = False)

  top_left2 = Point(300, 100)
  bottom_right2 = Point(500, 300)
  cell2 = Cell(win, has_left_wall = False)

  cell.draw(top_left.x, top_left.y, bottom_right.x, bottom_right.y)
  cell2.draw(top_left2.x, top_left2.y, bottom_right2.x, bottom_right2.y)
  cell.draw_move(cell2)

  win.wait_for_close()