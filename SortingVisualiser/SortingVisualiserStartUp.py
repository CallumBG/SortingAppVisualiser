import pygame
import SortingVisualiser.Buttons.ButtonFactory as buttonFactory
import SortingVisualiser.StaticFiles.Colors as Colors
import SortingVisualiser.Buttons.ButtonManager as buttonManager
import SortingVisualiser.Services.InputChecker as inputChecker
import SortingVisualiser.GuiManager.GUIManager as GUIManager
import SortingVisualiser.Sorting.SortingManager as sortingManager
import SortingVisualiser.ApplicationSettings.Settings as settings
import SortingVisualiser.Bars.BarManager as barManager


buttonList = []

#Starts the program
def Start(dis):
    clock = pygame.time.Clock()
    gameRunning = True
    dis.fill(Colors.white)
    #Creates 50 bars by default on the main menu
    barManager.createInitalBars(50)
    #List containing the buttons on the screen #createbars,setsort, sort, start
    buttonList = buttonFactory.createButtons(dis)
    while gameRunning:
        clock.tick(settings.FPS)
        dis.fill(Colors.white)
        inputChecker.checkInput(buttonList)
        buttonManager.highlightButtons(dis, barManager.numberSelected, barManager.sortSelected)
        #Render buttons
        for button in buttonList:
            button.render(dis)
        GUIManager.createGUI(dis)
        barManager.drawBars(dis, barManager.bars)
        pygame.display.update()