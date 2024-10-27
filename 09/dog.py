class Dog:

    def __init__(self, breed, age, name, has_owner=True):
        self.breed = breed
        self.age = age
        self.name = name
        self.has_owner = has_owner


    def bark(self):
        print(f"{self.name} barks at the moon.")



shiba_dog = Dog(breed="shiba inu",
                age = 1,
                name = "Yumyum",
                has_owner=True)

print(shiba_dog.__dict__)
print(Dog.__dict__)