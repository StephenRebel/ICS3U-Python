class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print("meow")

    def purr(self):
        return "purr"

    def multiply_3(self, x):
        return x * 3

    def get_name(self):
        return self.name

    def pet_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

c = Cat("King", 4)
c.set_age(5)
print(f"{c.get_name()} is {c.pet_age()} years old.")
c2 = Cat("Oreo", 7)
print(f"{c2.get_name()} is {c2.pet_age()} years old.")

"""
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Students("Tim", 17, 96)
s2 = Students("Danie", 17, 94)
s3 = Students("Andrew", 17, 89)
s4 = Students("Hunter", 16, 65)
s5 = Students("Autumn", 12, 73)

course = Course("Computer_Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.add_student(s5)
print(course.get_average_grade())
"""

"""
class Cat:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def Speak(slef):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Speak(self):
        print("Bark")
"""

#Could do all the above or

"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.colour}.")

class Dog(Pet):
    def speak(self):
        print("Woof")

class Fish(Pet):
    pass

p = Pet("King", 7)
p.show()
p.speak()
c = Cat("Oreo", 12, "black")
c.show()
c.speak()
d = Dog("Rosie", 16)
d.show()
d.speak()
f = Fish("Bubbles", 3)
f.show()
f.speak()
"""

"""
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("Bill")
p2 = Person("Hamza")
print(Person.number_of_people_())
"""

"""
class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")
    
print(f"{Math.add5(5)}, {Math.add10(5)}")
Math.pr()
"""