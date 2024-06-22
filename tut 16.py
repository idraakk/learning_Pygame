'''
* Changing position of food after having got eaten
* Added score in output
* adding Escape key that pauses the game
'''

'''
note: COMPLETE PROGRAM TILL NOW 
'''

import pygame
import random
pygame.init()

# Creating game window
width=600
height=600
gameWindow= pygame.display.set_mode((width,height)) #making the window obect with parameters width and height

#Game title
pygame.display.set_caption("Snake game by Idraak")
pygame.display.update() #used when anything is updated in game window, otherwise window will not be updated

#Game specific variables
exitGame = False
quitGame = False
wall_thickness=10
snake_length=10
snake_x=random.randrange(wall_thickness,width-wall_thickness-snake_length,10)
snake_y=random.randrange(wall_thickness,height-wall_thickness-snake_length,10)
direction='s'
old_direction='s'
velocity=5
food_x=random.randrange(wall_thickness,width-wall_thickness,10)
food_y=random.randrange(wall_thickness,height-wall_thickness,10)
food_length=10
fps=30
score=0

#Colour variables
red= (255, 0, 0) #By RGB convention. Max=255
white= (255, 255, 255)
black= (0, 0, 0)
grey= (128, 128, 128)

#clock for defining fps in future coding
clock = pygame.time.Clock()

#Game loop
while not exitGame:
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      exitGame= True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        if not direction == 'l' : #snake game rules- cannot change direction by 180 degrees
          direction='r'
      elif event.key == pygame.K_LEFT:
        if not direction == 'r' : #snake game rules- cannot change direction by 180 degrees
          direction='l'
      elif event.key == pygame.K_UP:
        if not direction == 'd' : #snake game rules- cannot change direction by 180 degrees
          direction='u'
      elif event.key == pygame.K_DOWN:
        if not direction == 'u' : #snake game rules- cannot change direction by 180 degrees
          direction='d'
      elif event.key == pygame.K_ESCAPE:
        direction='s'
  if direction=='r':
    snake_x +=velocity
  elif direction=='l':
    snake_x -=velocity
  elif direction=='u':
    snake_y -=velocity
  elif direction=='d':
    snake_y +=velocity

  #Keeping background colour while. It will be inside game loop
  gameWindow.fill(white)

  #Drawing snake head
  pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_length,snake_length])
  #Draw food
  pygame.draw.rect(gameWindow, red, [food_x,food_y,food_length,food_length])

  # Draw the boundary walls
  pygame.draw.rect(gameWindow, red, [0, 0, width, wall_thickness])  # Top wall
  pygame.draw.rect(gameWindow, red, [0, 0, wall_thickness, height])  # Left wall
  pygame.draw.rect(gameWindow, red, [0, height - wall_thickness, width, wall_thickness])  # Bottom wall
  pygame.draw.rect(gameWindow, red, [width - wall_thickness, 0, wall_thickness, height])  # Right wall

  # incrementing score
  if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6 :
    score+=1
    print("score:",score)
    food_x = random.randrange(wall_thickness, width - wall_thickness, 10)
    food_y = random.randrange(wall_thickness, height - wall_thickness, 10)


  pygame.display.update() # all updates together

  #defining fps in game
  clock.tick(fps)
