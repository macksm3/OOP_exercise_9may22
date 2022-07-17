# pet creation module to import
# parent class for all the pets to inherit from
class Pet:
    def __init__(self, name):
        self.name = name
        print("***New Pet Materializing!!!***")
        print()


# class definition of 'Dog' starts here
class Dog(Pet):
    # class attribute
    at1 = "mammal"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"I am a Dog. \nMy name is {self.name}, \nI am a {self.at1},"


# class definition of 'Cat' starts here
class Cat(Pet):
    # class attribute
    at1 = "mammal"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Cat. \nMy name is {self.name}. \nAnd I am a {self.at1}."


# class definition of 'Bird' starts here
class Bird(Pet):
    # class attribute
    at1 = "bird"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Parrot. \nMy name is {self.name}. \nI am a {self.at1}."


# class definition of 'Gecko' starts here
class Gecko(Pet):
    # class attribute
    at1 = "reptile"

    def __init__(self, name):
        super().__init__(name)

    # Instance method
    def speak(self):
        return f"Hello! \nI am a Gecko. \nMy name is {self.name}. \nAnd I am a {self.at1}."

