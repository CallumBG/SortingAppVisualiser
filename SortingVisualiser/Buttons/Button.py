import pygame
import SortingVisualiser.StaticFiles.Fonts as Fonts

import SortingVisualiser.StaticFiles.Colors as Colors;

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