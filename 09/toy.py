#SEPARATION OF CONCERNS

#real world example:
#class: egy leírás, ami alapján egy gép meg tudja csinálni a kívánt játékot
#__init__: a gép kezelőfelülete, ahol meg tudjuk adni hogy milyen típusú (pl: kisautó, baba stb.) és milyen színű játékot szeretnénk 
#instance: az osztály egy példánya, pl a gép által létrehozott játék
#instance variable: olyan tulajdonság, ami az adott példányt jellemzi: pl egy darab játék színe
#class variable: olyan tulajdonság, ami a teljes osztályra jellemző, pl: egy számláló arról, hány játékot gyártott már le a gépünk
#instance method: olyan metódus ami a példányokat használja/módosítja pl egy move() method ami mozgatja a játékot
#class method: olyan metódus ami az osztály attribútumait használja/módosítja
#static method: nincs hozzáférése sem a példányhoz, se az osztályhoz, de logikailag ide tartozik. megoszlanak a vélemények, hogy ez simán lehetne csak egy különálló function is minden esetben

class Toy:

    toy_count = 0

    def __init__(self, toy_type, toy_color):
        self.toy_type = toy_type
        self.toy_color = toy_color
        Toy.toy_count += 1

    def play(self):
        print(f"Currently playing with the {self.toy_color} {self.toy_type}")

    @classmethod
    def get_toy_count(cls):
        """Returns the total number of toys created."""
        return cls.toy_count

    @staticmethod
    def is_toy_safe_for_age(toy_type, age):
        """Checks if a toy is safe for a certain age group."""
        if toy_type == "small parts" and age < 3:
            return False
        return True



toy_1 = Toy("matchbox", "yellow")
print(toy_1)
print(toy_1.toy_color)
print(toy_1.toy_type)
toy_1.play()

#ismerős?

#name = "Steve"
#print(name.capitalize())


toy_1.toy_color = "green"
toy_1.play()