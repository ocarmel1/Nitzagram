from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from classes.Comment import Comment

def save_post(post, post_id, posts_file, comments_file):
    with open(posts_file, "a") as my_file:
        my_file.write("{}|".format(post_id) + post.to_list() + "\n")
    with open(comments_file, "a") as my_file:
        i = 0
        for comment in post.comments:
            my_file.write("{}|{}|{}".format(post_id, i, comment.comment) + "\n")

def load_all_posts(posts_file, comments_file):
    list_of_posts = []
    with open(posts_file, "r") as my_file:
        list_of_posts_lines = my_file.readlines()
        for line in list_of_posts_lines:
            array = line.split("|")
            if array[1] == "image":
                new_post = ImagePost(array[5][:len(array[5])-1],array[2],array[3])
                new_post.likes_counter = int(array[4])
                list_of_posts.append(new_post)

    with open(comments_file, "r") as my_file:
        list_of_comments = my_file.readlines()
        for line in list_of_comments:
            array = line.split("|")
            s = array[2][:len(array[2])-1]
            list_of_posts[int(array[0])].add_comment(Comment(array[2][:len(array[2])-1]))

    return  list_of_posts
