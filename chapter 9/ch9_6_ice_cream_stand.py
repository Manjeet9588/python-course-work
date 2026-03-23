'''An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"our resturant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The Resturant is open")

class Icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("The list of avialable flavors is : ")
        for flavor in self.flavors:
            print(f"\t--{flavor}")

ice_cream_stand = Icecreamstand("Taj Hotel", "Luxury", ['vanilla', 'chocolate', 'strawberry','Mint Chocolate Chip', 'Butter Pecan'])
ice_cream_stand.display_flavors()