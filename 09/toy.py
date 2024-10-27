#real life example: egy gépezet ami játékokat (pl matchbox, barbie baba stb.) gyárt
#van egy kezelőfelülete, amin be tudjuk állítani a következőket:
# - játék típusa
# - játék színe
#ezután a gép legyártja nekünk a játékot


#class: maga a gépezet, ami tudja hogyan kell a játékot megcsinálni a megadott paraméterek (típus, szín) alapján. Van egy blueprint (leírás) hozzá.
#__init__(): a gép kezelőfelülete, amivel interaktálunk amikor létre akarjuk hozni a játékot, itt egy gombnyomás hozza létre a játékot.
#instance: az osztály egy példánya, vagyis a gép által létrehozott 1 darab játék
#instance variable: olyan tulajdonság, ami egy gép által létrehozott játékra jellemző: pl játék színe
#class variable: olyan tulajdonság, ami a teljes osztályra (gépre) jellemző, pl: hány játékot gyártott már le
#instance method: olyan metódus, ami a példányokat (játékok) használja/módosítja: pl egy move() metódus ami által a játék mozog
#class method: olyan metódus ami az osztály attribútumait használja/változtatja pl: egy get_toy_count() method ami visszaadja az eddig legyártott játékok számát
#static method: nincs hozzáférése sem példányhoz, sem osztályhoz, de logikailag ide tartozik, pl: adott játék javasolt e n éves korban (is_toy_safe_for_age(toy_type, age) method) 

class Toy:

    toy_count = 0

    def __init__(self, toy_type, toy_color):
        self.toy_type = toy_type
        self.toy_color = toy_color
        Toy.toy_count += 1
    
    def play(self):
        print(f"Currently playing with the {self.toy_color} {self.toy_type}")

    def move(self, distance, direction):
        print(f"{self.toy_type} moved {distance} meters to the {direction}")

    @classmethod #dekorátor: megváltoztatja az alatta definiált function működését
    def get_toy_count(cls):
        return cls.toy_count

    @staticmethod
    def is_toy_safe_for_age(toy_type, age):

        if toy_type == "lego" and age < 3:
            return False
        return True




matchbox = Toy(toy_type="matchbox", toy_color="yellow")
print(matchbox)
print(matchbox.toy_color)
print(matchbox.toy_type)
matchbox.play()

barbie = Toy(toy_type="barbie", toy_color="pink")

barbie.toy_color = "green"
print(barbie.toy_color)
barbie.toy_color = "red"
print(barbie.toy_color)
barbie.play()

matchbox.move(3, "left")
print(Toy.toy_count)
print(Toy.get_toy_count())

print(Toy.is_toy_safe_for_age("matchbox", 10))


####

name = "steve"
print(name.capitalize())
print(str.capitalize("almafa"))
#EVERYTHING IS AN OBJECT IN PYTHON