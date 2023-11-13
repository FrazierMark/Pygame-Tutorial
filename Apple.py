from random import randint, choice
from constants import lanes, screen, fruits_captured
from GameObject import GameObject

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'images/apple.png')
    self.dx = 0
    self.dy = (randint(1, 200) / 100) + fruits_captured
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.y > 500 or self.y < -64:
      self.reset()
      self.dy = (randint(1, 200) / 100) + fruits_captured 
      self.dy *= choice([-1, 1])

  def reset(self):
    self.x = choice(lanes)
    self.y = choice([-64, 500])