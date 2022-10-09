import math
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return(f"Rectangle(width={self.width}, height={self.height})")
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      result = "Too big for picture."
    else:
      result = ""
      i = 0
      while(i < self.height):
        result += self.width * "*" + "\n"
        i += 1
    return result

  def get_amount_inside(self, rectangle):
    a = math.floor(self.width / rectangle.width)
    b = math.floor(self.height / rectangle.height)
    return a * b

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return(f"Square(side={self.width})")

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side