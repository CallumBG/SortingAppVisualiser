import SortingVisualiser.StaticFiles.Colors as Colors
import SortingVisualiser.StaticFiles.Fonts as Fonts
import SortingVisualiser.Bars.BarManager as barManager
import SortingVisualiser.Sorting.BubbleSort as bubbleSort
import SortingVisualiser.Sorting.SelectionSort as selectionSort
import SortingVisualiser.Sorting.InsertionSort as insertionSort
import SortingVisualiser.ApplicationSettings.Settings as settings
import pygame

#Updates the sort method array with the selected sort method
def setSortMethod(method):
    if method == "bubble":
        barManager.sortSelected = [True, False, False]
    elif method == "selection":
        barManager.sortSelected = [False, True, False]
    else:
        barManager.sortSelected = [False, False, True]
    
#Starts when the sort button is pressed, it then sorts based on the selected sort method
def Sort(dis):
    #Calls the sort method thats selected baed on the sortSelected list variable
    if barManager.sortSelected[0] == True:
        bubbleSort.bubbleSort(dis,barManager.bars)
    elif barManager.sortSelected[1] == True:
        selectionSort.selectionSort(dis)
    else:
        insertionSort.insertionSort(dis,barManager.bars)

#Displays the text and draws all bars green to show it's sorted
def completedSortSequence(dis, barList):
    text = "Sorted!"
    draw_text = Fonts.sortedFont.render(text, 1, Colors.black)
    j = 0
    #Draws all bars in barList in green
    while j <= len(barList) - 1:
        pygame.draw.rect(dis, Colors.black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
        pygame.draw.rect(dis, Colors.green, (50+ j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
        j += 1
    #Display sorted text
    dis.blit(draw_text, (settings.width/2 - draw_text.get_width()/2, settings.height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000) 
