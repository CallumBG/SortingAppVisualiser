#**Selection sort methods**
import SortingVisualiser.Sorting.SortingManager as sortingManager
import SortingVisualiser.GuiManager.GUIManager as GUIManager
import SortingVisualiser.ApplicationSettings.Settings as settings
import SortingVisualiser.Services.InputChecker as inputChecker
import SortingVisualiser.SortingVisualiserStartUp as sortingVisualiserStartUp
import SortingVisualiser.StaticFiles.Colors as Colors
import pygame
import SortingVisualiser.Buttons.ButtonFactory as buttonFactory
import SortingVisualiser.Bars.BarManager as barManager

pygame.init()

clock = pygame.time.Clock()

#Sorts using selection sort
def selectionSort(dis):
    buttonList = buttonFactory.createSortScreenButtons(dis)
    i = 0
    j = 0
    barList = barManager.bars
    #Traverses each element in the list
    for i in range (len(barList)):
        jMin = i
        #Traverses each element further in the list than element i
        for j in range (i+1, len(barList)):
            setSelectionSortRefreshRate(barList)
            inputChecker.checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
            #If selected element is smaller than current min, set it as the new min
            if(barList[j] < barList[jMin]):
                jMin = j
            updateSelectionSortBars(dis, barList, i, jMin, j)
        #Swap the current smallest element with the current element
        barList[i], barList[jMin] = barList[jMin], barList[i]
    #completedSortSequence(barList)
    sortingVisualiserStartUp.Start(dis)

#Updates the bars to show the visual representation of the selection sort
def updateSelectionSortBars(dis,barList, i, jMin, currentJ):
    updating = True
    while updating:
        GUIManager.createSortScreen(dis)
        j = 0
        #Draws each bar
        while j < len(barList):
            #Draws each bar thats already been sorted in green
            if j < i:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the current minimum element as blue
            elif j == jMin:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.blue, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the current inspected element as purple
            elif j == currentJ:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.purple, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the default bar red
            else:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
        pygame.display.update()
        updating = False

#Sets the refresh rate for each number of bars
def setSelectionSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(settings.FPS/20)
    elif len(barList) == 50:
        clock.tick(settings.FPS/3)
    elif len(barList) == 100:
        clock.tick(settings.FPS)
