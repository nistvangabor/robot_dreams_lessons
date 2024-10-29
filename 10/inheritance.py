class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")
              

#1. amit megmutatok:
#class Employee(Person): #jelenleg mindent örököl
#    pass


#2. amit megmutatok:
#class Employee(Person): #jelenleg mindent örököl
#    def __init__(self, f_name, l_name):
#        self.first_name = f_name
#        self.last_name = l_name

#3. amit megmutatok
#class Employee(Person):
#    def __init__(self, first_name, last_name):
#        super().__init__(first_name, last_name)


#4. amit megmutatok

class Employee(Person):
    def __init__(self, first_name, last_name, job_type):
        super().__init__(first_name, last_name)
        self.job_type = job_type

    def do_work(self):
        print(f"{self.first_name} is working as a {self.job_type}")

    def introduce_person(self): # METHOD OVERRIDING
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am a {self.job_type}")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
    def __eq__(self, other_obj:object):
        if isinstance(other_obj, Employee):
            return self.first_name == other_obj.first_name and self.last_name == other_obj.last_name
        return False   

p = Person(first_name="John", last_name="Smith")
print(p)
p.introduce_person()


e = Employee(first_name="Johnny", last_name="EmployeeSmith", job_type="programmer")
print(e)
e.introduce_person()
print(e.job_type)
e.do_work()
e.introduce_person()