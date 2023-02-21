from DOG import *

if __name__ == '__main__':
    dog_1 = Dog("Rex", "Labrador", 'Black', 2, 50, "Tom")
    dog_2 = Dog("Fifi", "chiuaua", 'Blonde', 2, 50, "Ren")

    dog_1.print_details()

    Dog.animal_type = "reptile"

    dog_1.print_details()
    dog_2.print_details()





