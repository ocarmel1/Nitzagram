class Dog:
    animal_type = "dog"

    def __init__(self, dog_name, dog_breed, dog_color, dog_age, dog_weight, dog_owner):
        self.name = dog_name
        self.breed = dog_breed
        self.color = dog_color
        self.age = dog_age
        self.weight = dog_weight
        self.owner = dog_owner

    def print_details(self):
        print(self.name, self.breed, self.color, self.age,
              self.weight, self.owner, self.animal_type)

