import pygame
import SortingVisualiser.SortingVisualiserStartUp as SortingVisualiserStartUp
import SortingVisualiser.ApplicationSettings.Settings as settings

#Initialises the pygame module
pygame.init()

dis = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption("Sorting Application")
SortingVisualiserStartUp.Start(dis)
