import pygame
import sys
from random import randint, choice, random


pygame.init()
lanes = [93, 218, 343]
screen = pygame.display.set_mode([500, 500])


class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.y > 500 or self.y < -64:
      self.reset()
      self.dy = (randint(0, 200) / 100) + 1 
      self.dy *= choice([-1, 1])

  def reset(self):
    self.x = choice(lanes)
    self.y = choice([-64, 500])



class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dy = 0
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x > 500 or self.x < -64:
      self.reset()
      self.dx = (randint(0, 200) / 100) + 1 
      self.dx *= choice([-1, 1])

  def reset(self):
    self.y = choice(lanes)
    self.x = choice([-64, 500])

class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'images/alien.png')
    self.dy = 0
    self.dx = (randint(0, 200) / 100) + 1
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
          self.dx = (randint(0, 200) / 100) + 1
          self.dx *= choice([-1, 1])  # Randomly choose left or right
          self.dy = 0
      else:  # Move vertically
          self.dy = (randint(0, 200) / 100) + 1
          self.dy *= choice([-1, 1])  # Randomly choose up or down
          self.dx = 0
      return direction



class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1 # new attribute
    self.pos_y = 1 # new attribute
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
  
  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]


apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

clock = pygame.time.Clock()

# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
      elif event.key == pygame.K_q:								# if Q is pressed, game quits.
        sys.exit()

  screen.fill((255, 255, 255))

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
  # Update the window

  pygame.display.flip()

  clock.tick(30)