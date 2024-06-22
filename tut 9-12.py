'''
* Background Colour
* Snake Head
* Moving snake head up down right and left one step with keys
* Defining fps with clock
'''

import pygame
pygame.init()

# Creating game window
width=900
height=600
gameWindow= pygame.display.set_mode((width,height)) #making the window obect with parameters width and height

#Game title
pygame.display.set_caption("Snake game by Idraak")
pygame.display.update() #used when anything is updated in game window, otherwise window will not be updated

#Game specific variables
exitGame = False
quitGame = False
snake_x=105
snake_y=300
snake_length=10
#Colour variables
red= (255, 0, 0) #By RGB convention. Max=255
white= (255, 255, 255)
black= (0, 0, 0)
fps = 30
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
        snake_x += 10
      elif event.key == pygame.K_LEFT:
        snake_x -= 10
      elif event.key == pygame.K_UP:
        snake_y -= 10 #the graph in screen starts from left and up
      elif event.key == pygame.K_DOWN:
        snake_y += 10
  
  #Keeping background colour while. It will be inside game loop
  gameWindow.fill(white)
  
  #Drawing snake head
  pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_length,snake_length])
  pygame.display.update() #background and snake update together
  
  #defining fps in game
  clock.tick(fps)
