import pygame
import pywhatkit
from classes.Post import Post
from helpers import from_text_to_array, screen, center_text
from constants import *

class TextPost(Post):
    def __init__(self, text, text_color, background_color, location, description):
        Post.__init__(self, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.text_array = from_text_to_array(text)

    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        for i in range(len(self.text_array)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text_array[i], True, self.text_color)
            screen.blit(text, center_text(len(self.text_array), text, i))

    def share(self, phnum):
        message = "The content of the post is {}.\nNumber of likes is {}.\nThe location is {}.\nThe description is {}".format(self.text,self.likes_counter,
                                                                                               self.location, self.description)
        pywhatkit.sendwhatmsg_instantly(phnum, message)

    def to_list(self):
        return "{}|{}|{}|{}".format("text", self.location, self.description, self.likes_counter)

