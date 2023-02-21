from constants import *
from helpers import screen
import pygame


class Filter:
    def __init__(self, color, level):
        self.color = color
        self.level = level
    def apply_filter(self):
        rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        rect.set_alpha(self.level)
        rect.fill(self.color)
        screen.blit(rect, (POST_X_POS, POST_Y_POS))
