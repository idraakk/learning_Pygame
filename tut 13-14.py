'''
* Giving velocity inside game loop
'''
#Game loop
while not exitGame:
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      exitGame= True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        direction='r'
      elif event.key == pygame.K_LEFT:
        direction='l'
      elif event.key == pygame.K_UP:
        direction='u'
      elif event.key == pygame.K_DOWN:
        direction='d'
  if direction=='r':
    snake_x +=velocity
  elif direction=='l':
    snake_x -=velocity
  elif direction=='u':
    snake_y -=velocity
  elif direction=='d':
    snake_y +=velocity
