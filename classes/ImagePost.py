import pygame
from constants import *
from classes.Post import Post
from helpers import screen
import pywhatkit


class ImagePost(Post):
    def __init__(self, image_src, location, description, filter = None):
        self.image_path = image_src
        Post.__init__(self, location, description)
        self.image = pygame.image.load(image_src)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))
        self.filter = filter

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        if (self.filter != None):
            self.filter.apply_filter()

    def share(self, phnum):
        message = "Number of likes is {}.\nthe location is {}.\nthe description is {}".format(self.likes_counter,
                                                                                               self.location, self.description)
        pywhatkit.sendwhats_image(phnum, self.image_path, message)


    def to_list(self):
        return "{}|{}|{}|{}|{}".format("image", self.location, self.description, self.likes_counter, self.image_path)

