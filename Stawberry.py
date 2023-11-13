from GameObject import GameObject
from constants import lanes, screen, fruits_captured
from random import randint, choice

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dy = 0
    self.dx = (randint(1, 200) / 100) + fruits_captured
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 500 or self.x < -64:
      self.reset()
      self.dx = (randint(1, 200) / 100) + fruits_captured 
      self.dx *= choice([-1, 1])

  def reset(self):
    self.y = choice(lanes)
    self.x = choice([-64, 500])