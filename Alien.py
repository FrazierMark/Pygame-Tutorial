from GameObject import GameObject
from constants import lanes, screen, fruits_captured
from random import randint, choice



class Alien(GameObject):
  def __init__(self):
    super(Alien, self).__init__(0, 0, 'images/alien.png')
    self.dy = 0
    self.dx = (randint(1, 200) / 100) + fruits_captured
    self.reset(lanes)

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
        self.randomize_directions()
        self.reset(lanes)

  def reset(self, lanes):
      direction = self.randomize_directions()
      if direction == 0:  # Moving horizontally
          self.y = choice(lanes)
          self.x = choice([-64, 500])
      else:  # Moving vertically
          self.x = randint(0, 500)  # Random x position within screen width
          self.y = choice([-64, 500])

  def randomize_directions(self):
      direction = randint(0, 1)
      if direction == 0:  # Move horizontally
          self.dx = (randint(1, 200) / 100) + fruits_captured
          self.dx *= choice([-1, 1])  # Randomly choose left or right
          self.dy = 0
      else:  # Move vertically
          self.dy = (randint(1, 200) / 100) + fruits_captured
          self.dy *= choice([-1, 1])  # Randomly choose up or down
          self.dx = 0
      return direction