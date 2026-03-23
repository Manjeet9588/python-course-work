'''Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''

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

user1 = User("Manjeet","saini", 20, "Jaipur")
user2 = User("Shubham","saini", 19, "Narnaul")
user3 = User("jahanvi","ramawat", 21, "udaipur")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
