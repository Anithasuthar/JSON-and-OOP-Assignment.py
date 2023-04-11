class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def play_fetch(self):
        print(f"{self.name} loves to play fetch.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def snore(self):
        print(f"{self.name} snores loudly.")



my_dog = Dog("Buddy", 5, "brown")
my_dog.description()
my_dog.get_info()

my_jrt = JackRussellTerrier("Max", 3, "white")
my_jrt.description()
my_jrt.get_info()
my_jrt.play_fetch()

my_bulldog = Bulldog("Maggie", 7, "gray")
my_bulldog.description()
my_bulldog.get_info()
my_bulldog.snore()
