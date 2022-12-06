from unicodedata import name


class animal:
    def __init__(self, name, gender, age, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
    
    def facts(self):
        print(f"Name: {self.name}\nage: {self.age}\ngender: {self.gender}\nweight: {self.weight}\n")


dog = animal("jerry", "male", 2, "200KG")
dog.facts()