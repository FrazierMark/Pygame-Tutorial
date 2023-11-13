import pygame
import sys
from random import randint, choice
from sounds import Sounds
from constants import lanes, screen, fruits_captured
from GameObject import GameObject
from Apple import Apple
from Alien import Alien
from Player import Player
from Star import Star
from Stawberry import Strawberry

pygame.init()



apple = Apple()
strawberry = Strawberry()
player = Player()
alien = Alien()

stars = []
for i in range(3):
  star = Star()
  stars.append(star)

clock = pygame.time.Clock()

# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(star)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(alien)


for star in stars:
  all_sprites.add(star)


fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

bg_music = Sounds()
bg_music.play_bg_music()

running = True

game_over = False

while running:
  
  # Fill the screen with the scaled background image
  bg_image = pygame.image.load('images/background.jpg')
  scaled_bg_image = pygame.transform.scale(bg_image, [500, 500])
  screen.blit(scaled_bg_image, (0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_q:
        running = False
      elif event.key == pygame.K_p and game_over:
        game_over = False
        fruits_captured = 0
        player.reset()
        apple.reset()
        strawberry.reset()
        alien.reset(lanes)
      elif not game_over:
        if event.key == pygame.K_LEFT:
          player.left()
        elif event.key == pygame.K_RIGHT:
          player.right()
        elif event.key == pygame.K_UP:
          player.up()
        elif event.key == pygame.K_DOWN:
          player.down()
      elif event.key == pygame.K_q:								# if Q is pressed, game quits.
        sys.exit()


  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
      fruits_captured += 0.2
      bg_music.play_collision_sound()
      fruit.reset()
      
    if not game_over:
      if pygame.sprite.collide_rect(player, alien):
        game_over = True

  if game_over:
    # Show the game over screen with a message
    game_over_message = pygame.font.Font(None, 36).render("Game Over! Press Q to quit.", True, (100, 0, 0))
    play_again_message = pygame.font.Font(None, 36).render("Or Press P to play again.", True, (100, 30, 0))
    screen.blit(game_over_message, (70, 100))
    screen.blit(play_again_message, (75, 150))
        

 
  pygame.display.flip()

  clock.tick(30)