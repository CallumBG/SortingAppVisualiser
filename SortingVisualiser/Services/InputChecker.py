import pygame

#Checks for user input on current buttons and quit button
def checkInput(buttonList):
    for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                pygame.quit()
                quit()
            for button in buttonList:
                button.get_event(event)