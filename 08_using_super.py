class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        self.subject = subject
        super().__init__(name)

t1 = Teacher("Talha", "Chemistry")
print(f"My name is {t1.name} and I am teaching {t1.subject}")