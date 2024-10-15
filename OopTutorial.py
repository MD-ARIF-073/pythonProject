
def method_name(a,b):
    print("A method")

class Person:
    def __init__(self, person_name):
        self.name = person_name                 # class Peson er instance er ekta variable

    def get_name(self):
        return self.name

method_name(10, 20)
a_person  = Person("Sani")
b_person = Person("Arif")

print(a_person.get_name())
print(b_person.get_name())

