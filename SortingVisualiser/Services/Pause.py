import pygame
import SortingVisualiser.ApplicationSettings.Settings as settings
import SortingVisualiser.Buttons.ButtonFactory as buttonFactory
import SortingVisualiser.Services.InputChecker as inputChecker

pygame.init()

clock = pygame.time.Clock()

#Sets weather the program is paused
paused = False

#Pauses the program and creates a play button to restart the program
def pause(dis):
    global paused
    buttonList = buttonFactory.createSortScreenButtons(dis)
    #Updates the global variable if already paused
    if paused == True:
        paused = False
    else:
        paused = True
    #If not paused enter the paused mode
    while paused:
        clock.tick(settings.FPS)
        inputChecker.checkInput(buttonList)
        for button in buttonList:
            button.render(dis)
        pygame.display.update()