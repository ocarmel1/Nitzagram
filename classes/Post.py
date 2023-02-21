import pygame
import os
from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    user_name = "Ohad Carmel"

    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        pass


    @staticmethod
    def display_text(font, size, text, color, x, y):
        font = pygame.font.SysFont(font, size)
        text = font.render(text, True, color)
        screen.blit(text, [x, y])

    def display_header(self):
        # Display user name
        self.display_text('chalkduster.ttf', 15, self.user_name, (50, 50, 50), USER_NAME_X_POS, USER_NAME_Y_POS)
        # Display location
        self.display_text('chalkduster.ttf', 15, self.location, (134, 134, 134), LOCATION_TEXT_X_POS,
                          LOCATION_TEXT_Y_POS)
        # Display description
        self.display_text('chalkduster.ttf', 15, self.description, (50, 50, 50), DESCRIPTION_TEXT_X_POS,
                          DESCRIPTION_TEXT_Y_POS)

    def display_likes(self):
        # Display likes
        likes_text = "Liked by {} users".format(self.likes_counter)
        self.display_text('chalkduster.ttf', 15, likes_text, (0, 0, 0), LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS)

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def view_more_comments(self):
        self.comments_display_index = self.comments_display_index + 1 \
            if (self.comments_display_index + 1 < len(self.comments) - 1) else 0

    def reset_comments_display_index(self):
        self.comments_display_index = 0
