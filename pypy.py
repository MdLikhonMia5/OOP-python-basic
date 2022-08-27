class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def get_summary(self):
        return f"Name: {self.__name}, Age: {self.__age}"

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry person cant have a number")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string

son = Person("Y$SIN",12)

person_list = [
    Person("Ease", 21),
    Person("Sohan", 22)
]
for person in person_list:
    if person.getAge() > 10:
        print(person.get_summary())



