import pygame
import SortingVisualiser.StaticFiles.Fonts as Fonts
import SortingVisualiser.StaticFiles.Colors as Colors
import SortingVisualiser.ApplicationSettings.Settings as settings


#Creates the basic color and text of the main menu
def createGUI(dis):
    numberText = "Number to sort: "
    sortText = "Sort method: "
    numberText = Fonts.font_style.render(numberText, True, Colors.black)
    sortText = Fonts.font_style.render(sortText, True, Colors.black)
    pygame.Surface.blit(dis, numberText, (10, 20))
    pygame.Surface.blit(dis, sortText, (30, 90))
    pygame.draw.rect(dis, Colors.black,(43.5,140,settings.width - 87, settings.height - 150))
    pygame.draw.rect(dis, Colors.white,(48.5,145,settings.width - 97, settings.height - 160))

#Creates the basic color and text of the sort screen
def createSortScreen(dis):
    sortingText = "Sorting... "
    sortingText = Fonts.sortedFont.render(sortingText, True, Colors.black)
    pygame.Surface.blit(dis, sortingText, (300, 40))
    pygame.draw.rect(dis, Colors.black,(43.5,140,settings.width - 87, settings.height - 150))
    pygame.draw.rect(dis, Colors.white,(48.5,145,settings.width - 97, settings.height - 160))