''' Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''


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

class Privileges():
    def __init__(self,privileges = None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user","can make new rules"]
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        print("The privileges of an Admin is : ")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()
        



admin = Admin("Manjeet","saini",20,"narnaul")
admin.privileges.show_privileges()


