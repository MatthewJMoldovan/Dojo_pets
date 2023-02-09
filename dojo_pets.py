class Ninja():

    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Meowzers", "Cat", "Bakin Biscuits")

    def display_ninja_info(self):
        print(self.first_name)
        print(self.last_name)
        self.pet.display_pet_info()

    def walk(self):
        print(f"{self.pet.name} time for a walk!")
        self.pet.play()

    def bathe(self):
        print(f"{self.pet.name} It's bath time!")
        self.pet.noise("rawr")

    def feed(self):
        print(f"{self.pet.name} time for some {self.pet_food}!")
        self.pet.eat()



class Pet():

    def __init__(self, name, type, tricks, health = 50, energy = 50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(f"{self.name} snuggles up for a nappy")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s Healh increased to: {self.health}")
        print(f"{self.name}'s Energy increased to: {self.energy}")

    def play(self):
        self.health += 5
        print(f"{self.name}'s Healh increased to: {self.health}")

    def noise(self, sound):
        print(f"{self.name} lets out a {sound}")

    def display_pet_info(self):
        print(self.name)
        print(self.type)
        print(self.tricks)
        print(f"{self.name}'s Healh is at: {self.health}")
        print(f"Energy is at: {self.energy}")


ninja1 = Ninja("Matt","Moldovan","sardines","kibble",)

ninja1.display_ninja_info()
ninja1.walk()
ninja1.bathe()
ninja1.feed()
