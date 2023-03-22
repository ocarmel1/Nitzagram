import os
from classes.Comment import Comment
from classes.Filter import Filter
from helpers import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from buttons import *
from helpers import mouse_in_button
from files_bonus import *
import os


def censor(bad_words_list , comment):
    print(1)
    words_array = comment.split()
    new_string = ""
    for word in words_array:
        if not word in bad_words_list:
            new_string = new_string + word + " "
        else:
            new_string = new_string + "*"*len(word) + " "
    # for word in comment.split():
    #     if word in bad_words_list:
    #         word = "*"*len(word)
    # print(comment)
    # return comment


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    # first_post = ImagePost('Images/noa_kirel.jpg','Beer Sheva!!!!','Noa Kirel with friends',Filter((100,20,15),80))
    # second_post = ImagePost('Images/ronaldo.jpg', 'United Arab', 'Noa Kirel with friends')
    # third_post = ImagePost('Images/DSC_0320.JPG', 'Georgia', 'Noa Kirel with friends')
    forth_post = TextPost("This is my first try!", (121, 65, 42), (240, 32, 159), "Beer Sheva!", "Just trying to code")
    # posts_list = [first_post, second_post, third_post, forth_post]
    current_index = 0
    # current_post = posts_list[current_index]

    # assign directory
    directory = 'Images'

    # iterate over files in
    # that directory
    posts_path = r"DB\posts.txt"
    comments_path = r"DB\comments.txt"
    new_posts_list = []
    if os.path.exists(posts_path):
        new_posts_list = load_all_posts(posts_path,comments_path)
    else:
        for filename in os.listdir('Images'):
            f = os.path.join('Images', filename)
            # checking if it is a file
            if os.path.isfile(f) and f != r"Images\background.png":
                new_posts_list.append(ImagePost(f,"bla bla bla", "ohad",Filter((100,20,15),80)))
    new_posts_list.append(forth_post)
    current_post = new_posts_list[current_index]






    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if os.path.exists(posts_path):
                    os.remove(posts_path)
                if os.path.exists(comments_path):
                    os.remove(comments_path)
                i = 0
                for post in new_posts_list:
                    save_post(post, i, posts_path, comments_path)
                    i += 1
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, mouse_pos):
                    current_post.add_like()
                elif mouse_in_button(comment_button, mouse_pos):

                    new_comment = censor(BAD_WORDS, read_comment_from_user())
                    new_comment = Comment(new_comment)
                    current_post.add_comment(new_comment)
                elif mouse_in_button(click_post_button, mouse_pos):
                    current_post.reset_comments_display_index()
                    current_post = new_posts_list[current_index]
                    #  current_index = [0, current_index+1][current_index+1 == len(posts_list)]
                    current_index = current_index + 1 if current_index+1 < len(new_posts_list) else 0
                elif mouse_in_button(view_more_comments_button, mouse_pos):
                    current_post.view_more_comments()
                elif mouse_in_button(button_share, mouse_pos):
                    current_post.share(read_comment_from_user())

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
