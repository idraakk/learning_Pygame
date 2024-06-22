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

#Colour variables
red= (255, 0, 0) #By RGB convention. Max=255
white= (255, 255, 255)
black= (0, 0, 0)

#Game loop
while not exitGame:
  for event in pygame.event.get():
    #print(event) 
    if event.type == pygame.QUIT:
      exitGame= True
  #Keeping background colour while. It will be inside game loop
  gameWindow.fill(white)
  pygame.display.update()
