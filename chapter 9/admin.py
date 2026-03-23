from user import User

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



