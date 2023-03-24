#**Bubble sort methods**
import SortingAppProgram.Sorting.SortingManager as sortingManager
import SortingAppProgram.GuiManager.GUIManager as GUIManager
import SortingAppProgram.ApplicationSettings.Settings as settings
import SortingAppProgram.Services.InputChecker as inputChecker
import SortingAppProgram.SortingVisualiserStartUp as SortingAppProgramStartUp
import SortingAppProgram.StaticFiles.Colors as Colors
import pygame
import SortingAppProgram.Buttons.ButtonFactory as buttonFactory
import SortingAppProgram.Bars.BarManager as barManager

pygame.init()

clock = pygame.time.Clock()

#Sort using bubble sort method
def bubbleSort(dis, newList):
    i = 0
    buttonList = buttonFactory.createSortScreenButtons(dis)
    #Travers through each element in the list
    while i < len(newList):
        inputChecker.checkInput(buttonList)
        for button in buttonList:
            button.render(dis)
        #Flag element to check if any changes have been made
        flag = 0
        j = 0
        #Traverses through each element before the end sorted element
        while j + i < (len(newList) - 1):
            inputChecker.checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
                #If current element is larger than the element after, swap them
                if newList[j ] > newList[j +1]:
                    higherNum = newList[j ]
                    newList[j] = newList[j +1]
                    newList[j +1] = higherNum
                    flag += 1 
                #Draw the new updated list of bars
                updateBubbleSortBars(dis,newList, j, i)
            j += 1
        #If no changes are made, the list is sorted, so end
        if flag == 0:
            break
        i += 1
    #Ensures i is the end element, incase the list is sorted early
    i = len(newList)
    updateBubbleSortBars(dis,newList, j, i)
    sortingManager.completedSortSequence(dis,newList)
    SortingAppProgramStartUp.Start(dis)

#Updates the bars to show the visual representation of the bubble sort
def updateBubbleSortBars(dis,barList,passedJ, passedI):
    updating = True
    while updating:
        setBubbleSortRefreshRate(barList)
        GUIManager.createSortScreen(dis)
        j = 0
        #Draws all the bars
        while j < len(barList):
            #If the bar is sorted, draw in green
            if j >= len(barList) - passedI:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the current element as blue
            elif j-1 == passedJ:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.blue, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the bar in red by default
            else:
                pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, Colors.red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
                
        updating = False
    pygame.display.update()

#Sets the refresh rate for each number of bars
def setBubbleSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(settings.FPS/5)
    elif len(barList) == 50:
        clock.tick(settings.FPS)
    elif len(barList) == 100:
        clock.tick(settings.FPS*4)
