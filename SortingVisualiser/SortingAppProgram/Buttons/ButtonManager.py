import pygame
import SortingAppProgram.StaticFiles.Colors as Colors

#Highlights each selected buttton green
def highlightButtons(dis, numberSelected, sortSelected):
    #Depending on which button is selected it adds a green rectange slightly wider than the original button
    if numberSelected[0] == True:
        pygame.draw.rect(dis, Colors.green, (195, 5, 160, 60))
    elif numberSelected[1] == True:
        pygame.draw.rect(dis, Colors.green, (355, 5, 160, 60))
    else:
        pygame.draw.rect(dis, Colors.green, (515, 5, 185, 60))
    if sortSelected[0] == True:
        pygame.draw.rect(dis, Colors.green, (175, 75, 160, 60))
    elif sortSelected[1] == True:
        pygame.draw.rect(dis, Colors.green, (335, 75, 180, 60))
    else:
        pygame.draw.rect(dis, Colors.green, (515, 75, 185, 60))  