import pygame
import SortingAppProgram.Buttons.ButtonFactory as buttonFactory
import SortingAppProgram.StaticFiles.Colors as Colors
import SortingAppProgram.Buttons.ButtonManager as buttonManager
import SortingAppProgram.Services.InputChecker as inputChecker
import SortingAppProgram.GuiManager.GUIManager as GUIManager
import SortingAppProgram.Sorting.SortingManager as sortingManager
import SortingAppProgram.ApplicationSettings.Settings as settings
import SortingAppProgram.Bars.BarManager as barManager


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