from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class Rectangle(BaseModel):
  x: int
  y: int
  w: int
  h: int

class TextBox:
  __rect: Rectangle
  __curx: int
  __cury: int
  def __init__(self, rect: Rectangle):
    self.__rect = rect
  def print(self, text: str):
    for i in range(len(str)):
      print(str[i])
