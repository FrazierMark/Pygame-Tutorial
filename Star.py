from GameObject import GameObject
from constants import lanes, screen
from random import randint, choice

class Star(GameObject):
 def __init__(self):
   super(Star, self).__init__(0, 0, 'images/star.png')
   self.dx = (randint(0, 200) / 100) + 1
   self.dy = 0
   self.reset()

 def move(self):
   self.x += self.dx
   # Check the y position of the apple
   if self.x > 550: 
     self.reset()

 # add a new method
 def reset(self):
   self.x = -80
   self.y = choice(lanes)