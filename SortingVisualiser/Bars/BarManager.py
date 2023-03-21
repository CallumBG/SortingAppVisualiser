import random
import pygame
import SortingVisualiser.StaticFiles.Colors as Colors
import SortingVisualiser.ApplicationSettings.Settings as settings

#Default number in case no variable passed in
number = 50

#Sets which number of bars is selected
numberSelected = [False, True, False]

#Sets which sort is selected
sortSelected = [True, False, False]

#The list that holds the bars to be drawn
bars = []

#Initialises the number of bars selected with a random value
def createInitalBars(number):
    global numberSelected
    #Sets number to selected number
    if number == 10:
        numberSelected = [True, False, False]
    elif number == 50:
        numberSelected = [False, True, False]
    else:
        numberSelected = [False, False, True]
    #Sets barwidth to size of interface - 100 for borders
    barWidth = (settings.width-100)//number
    #Temporary list to hold the newly created bars
    barList = []
    i = 0
    #Creates the number of bars selected, with a random value to each and adds it to barList
    while i <= number - 1:
        tempBarHeight = random.randrange(0,round(settings.height-160), 1)
        tempBar = [barWidth, tempBarHeight]
        barList.append(tempBar)
        i += 1
    #Sets the global variable bars to the new list barList
    global bars 
    bars = barList

#Initialises the number of bars selected with a random value
def createBars(number):
    global numberSelected
    #Sets number to selected number
    if number == 10:
        numberSelected = [True, False, False]
    elif number == 50:
        numberSelected = [False, True, False]
    else:
        numberSelected = [False, False, True]
    #Sets barwidth to size of interface - 100 for borders
    barWidth = (settings.width-100)//number
    #Temporary list to hold the newly created bars
    barList = []
    i = 0
    #Creates the number of bars selected, with a random value to each and adds it to barList
    while i <= number - 1:
        tempBarHeight = random.randrange(0,round(settings.height-160), 1)
        tempBar = [barWidth, tempBarHeight]
        barList.append(tempBar)
        i += 1
    #Sets the global variable bars to the new list barList
    global bars
    bars = barList

    #Draws the bars that have been initialised
def drawBars(dis, barList):
    j = 0
    #Draws all the buttons in the barList
    while j <= len(barList) - 1:
        pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
        pygame.draw.rect(dis, Colors.red, (50+ j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
        j += 1