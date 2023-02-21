import pygame
from constants import *
from helpers import screen


class Comment:
    def __init__(self, comment):
        self.comment = comment

    def display(self, comment_num):
        # Display comment
        comment_font = pygame.font.SysFont('chalkduster.ttf', 15)
        comment_color = (0, 0, 0)
        comment_text = comment_font.render(self.comment, True, comment_color)
        screen.blit(comment_text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS+COMMENT_LINE_HEIGHT*comment_num])