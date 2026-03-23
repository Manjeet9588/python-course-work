class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.city = city.title()
    
    def describe_user(self):
        print(f"User : {self.first_name} {self.last_name}")
        print(f"Age : {self.age}")
        print(f"City : {self.city}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")