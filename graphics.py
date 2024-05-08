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
