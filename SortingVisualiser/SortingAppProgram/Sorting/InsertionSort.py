#**Insertion sort methods**
import SortingAppProgram.Sorting.SortingManager as sortingManager
import SortingAppProgram.GuiManager.GUIManager as GUIManager
import SortingAppProgram.ApplicationSettings.Settings as settings
import SortingAppProgram.Services.InputChecker as inputChecker
import SortingAppProgram.SortingVisualiserStartUp as SortingAppProgramStartUp
import SortingAppProgram.Sorting.SortingManager as sortingManager
import SortingAppProgram.StaticFiles.Colors as Colors
import pygame
import SortingAppProgram.Buttons.ButtonFactory as buttonFactory
import SortingAppProgram.Bars.BarManager as barManager

pygame.init()

clock = pygame.time.Clock()

#Sorts using insertion sort method
def insertionSort(dis,barList):
    # Traverse through 1 to len(barList)
    buttonList = buttonFactory.createSortScreenButtons(dis)
    for i in range(1, len(barList)):
        key = barList[i]
        # Move elements of barList[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < barList[j] :
            inputChecker.checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
            barList[j + 1] = barList[j]
            j -= 1
            #Draw the updated bars
            updateInsertionSortBars(dis,barList, i, j, key)
        #The next element is now the key to compare
        barList[j + 1] = key
    GUIManager.createSortScreen(dis)
    sortingManager.completedSortSequence(dis,barList)
    SortingAppProgramStartUp.Start(dis)

#Updates the bars to show the visual representation of the insertion sort
def updateInsertionSortBars(dis,barList, passedI, passedJ, key):
    updating = True
    while updating:
        setInsertionSortRefreshRate(barList)
        GUIManager.createSortScreen(dis)
        j = 0
        #Draw all bars in barList
        while j < len(barList):
            #If the element is the current largest element thats been inserted draw in green
            if j == passedI:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the current element thats being inserted in blue
            elif j == passedJ + 1:
                pygame.draw.rect(dis, Colors.black, (50 + j*key[0]-1, 145, key[0]-1, key[1]+1))
                pygame.draw.rect(dis, Colors.blue, (50 + j*key[0], 145, key[0]-3, key[1]))
                j += 1
            #Draw the bar red by default
            else:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
                
        updating = False
    pygame.display.update() 

#Sets the refresh rate for each numbher of bars
def setInsertionSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(settings.FPS/30)
    elif len(barList) == 50:
        clock.tick(settings.FPS/2)
    elif len(barList) == 100:
        clock.tick(settings.FPS)
