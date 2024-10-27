
#Encapsulation is one of the core principles of object-oriented programming (OOP) that involves bundling the data (attributes) and methods
#  (functions) that operate on the data into a single unit, or class. It restricts direct access to some of an object's components,
#  which is a means of preventing unintended interference and misuse of the methods and data.

#PUBLIC:

class Test:

    def __init__(self, a, b):
        self.a = a #public
        self.b = b #public

    def test_method(self):
        print("This is a public method.")

t = Test(1,2)
t.test_method()

#PROTECTED: csak az adott osztályból és a child osztályokból érhető el az információ
class Test:

    def __init__(self, a, b):
        self._a = a #protected
        self._b = b #protected

    def _test_method(self):
        print("This is a protected method.")
    
    #getter
    def get_a(self):
        return self._a

    def set_a(self, new_a):
        if new_a > 10:
            raise ValueError("Invalid")
        self._a = new_a
    

t = Test(2,3)
t._test_method()

#PRIVATE: csak az adott osztályokban érhető el az információ

class Test:

    def __init__(self, a, b):
        self.__a = a #protected
        self.__b = b #protected

    def __test_method(self):
        print("This is a protected method.")

    

t = Test(2,3)
t.__test_method()
