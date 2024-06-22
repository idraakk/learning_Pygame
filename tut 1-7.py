import pygame
pygame.init()

#Creating game window
pygame.display.set_mode((1200,600))
pygame.display.set_caption("My First Game")


#Game specific variables
exitGame= False
gameOver= False

#Game loop
while not exitGame:
    for event in pygame.event.get(): # pygame.event.get() gives a list of all mouse and keyboard events in real time inside the while loop
        print(event) #This prints all the events #cool
        if event.type == pygame.QUIT: #Event for clicking on Cross on the window
            exitGame= True
        if event.type == pygame.KEYDOWN: #Key pressed
            if event.key == pygame.K_RIGHT: #event.key only when a key is pressed. returns the pressed key
            
pygame.quit()
quit() #python quit function

'''
# Events

There are a lot of events like:

## General Events

| Event             | Attributes               |
|-------------------|--------------------------|
| QUIT              | none                     |
| ACTIVEEVENT       | gain, state              |
| KEYDOWN           | key, mod, unicode, scancode |
| KEYUP             | key, mod                 |
| MOUSEMOTION       | pos, rel, buttons        |
| MOUSEBUTTONDOWN   | pos, button              |

And many more!

## Joystick Events

There are events even for joystick:

| Event             | Attributes                   |
|-------------------|------------------------------|
| JOYAXISMOTION     | joy (deprecated), instance_id, axis, value |
| JOYBALLMOTION     | joy (deprecated), instance_id, ball, rel   |
| JOYHATMOTION      | joy (deprecated), instance_id, hat, value   |
| JOYBUTTONUP       | joy (deprecated), instance_id, button       |
| JOYBUTTONDOWN     | joy (deprecated), instance_id, button       |

'''
