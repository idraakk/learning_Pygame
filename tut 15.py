'''
* Updated changing direction function by adding a rule that the snake cannot rotate by 180 degrees in a single step
* Added boundary walls
* Updated the snake_x and snake_y algorithm that doesn't coicinde with boundary walls and generates a number which is multiple of 10 for better cleanliness
* Added food. In a way that it doesn't coicinde with boundary walls and generates a number which is multiple of 10 for better cleanliness
'''

'''
note: ADDED ONLY THE UPDATES and NOT THE ACTUAL COMPLETE CODE
'''

import random

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

#added a colour variable
grey= (128, 128, 128)

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
  if direction=='r':
    snake_x +=velocity
  elif direction=='l':
    snake_x -=velocity
  elif direction=='u':
    snake_y -=velocity
  elif direction=='d':
    snake_y +=velocity

  #Keeping background colour white. It will be inside game loop
  gameWindow.fill(white)

  #Drawing snake head
  pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_length,snake_length])
  pygame.draw.rect(gameWindow, red, [food_x,food_y,food_length,food_length])

  # Draw the boundary walls
  pygame.draw.rect(gameWindow, red, [0, 0, width, wall_thickness])  # Top wall
  pygame.draw.rect(gameWindow, red, [0, 0, wall_thickness, height])  # Left wall
  pygame.draw.rect(gameWindow, red, [0, height - wall_thickness, width, wall_thickness])  # Bottom wall
  pygame.draw.rect(gameWindow, red, [width - wall_thickness, 0, wall_thickness, height])  # Right wall

  pygame.display.update() # all updates together

  #defining fps in game
  clock.tick(fps)
