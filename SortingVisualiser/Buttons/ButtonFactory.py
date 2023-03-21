
import SortingVisualiser.StaticFiles.Colors as Colors
import SortingVisualiser.StaticFiles.Fonts as Fonts
import pygame
import SortingVisualiser.Bars.BarManager as barManager
import SortingVisualiser.Sorting.SortingManager as sortingManager
import SortingVisualiser.Services.Pause as pause
import SortingVisualiser.SortingVisualiserStartUp as sortingVisualiserStartUp

pygame.init()

#Buttons class which can execute a method when pressed
class Button:
    def __init__(self, rect, text, leftShift, color, command1, argument1 = None):
        text = Fonts.font_style.render(text, True, Colors.yellow)
        self.color = color
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(self.color)
        self.image.blit(text, [self.rect.size[0]/2 - leftShift, self.rect.size[1]/2 - 15])
        self.command1 = command1
        self.argument1 = argument1
    def render(self, screen):
        screen.blit(self.image, self.rect)
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if self.argument1 == None:
                    self.command1()
                else:
                    self.command1(self.argument1)

#Creates the buttons for the sort screen
def createSortScreenButtons(dis):
    pauseButton = Button((700,80, 100,50), "Pause", 30, Colors.red, pause.pause, dis) #pausemethod
    resetButton = Button((815,50, 80,50), "Reset", 30, Colors.red, sortingVisualiserStartUp.Start, dis) #StartMethod
    buttonList = [pauseButton, resetButton] 
    return buttonList

#Initialises the buttons to be used in the main menu
def createButtons(dis):
    tenValueButton = Button((200, 10, 150, 50), "10", 20, Colors.red, barManager.createBars, 10)
    fiftyValueButton = Button((360, 10, 150, 50), "50", 20, Colors.red, barManager.createBars, 50)
    oneHundredValueButton = Button((520, 10, 175, 50), "100", 20, Colors.red, barManager.createBars, 100)
    bubbleSortButton = Button((180, 80, 150, 50), "Bubble sort", 65, Colors.red, sortingManager.setSortMethod, "bubble")
    SelectionSortButton = Button((340, 80, 170, 50), "Selection sort", 75, Colors.red, sortingManager.setSortMethod, "selection")
    InsertionSortButton = Button((520, 80, 175, 50), "Insertion sort", 75, Colors.red, sortingManager.setSortMethod, "insertion")
    sortButton = Button((700, 10, 100,50), "Sort", 30, Colors.red, sortingManager.Sort, dis)
    resetButton = Button((815,50, 80,50), "Reset", 30, Colors.red, sortingVisualiserStartUp.Start, dis)
    buttonsList = [tenValueButton,oneHundredValueButton,fiftyValueButton,bubbleSortButton, SelectionSortButton,InsertionSortButton,sortButton, resetButton]
    return buttonsList
