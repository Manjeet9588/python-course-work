'''An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.'''


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

class Admin(User):
    def __init__(self, first_name, last_name, age, city, privileges):
        super().__init__(first_name, last_name, age, city,)
        self.privileges = privileges
    
    def show_privileges(self):
        print("The privileges of an Admin is : ")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

admin = Admin("Manjeet","saini",20,"narnaul",["can add post", "can delete post", "can ban user","can make new rules"])

admin.show_privileges()