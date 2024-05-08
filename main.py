from graphics import Window, Point, Line

if __name__ == "__main__":
  win = Window(800, 600)
  
  start = Point(100, 100)
  end = Point(300, 300)
  line = Line(start, end)

  win.draw_line(line = line, fill_color = "black")

  win.wait_for_close()