''' Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Our resturant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"The Resturant is open")

Restaurant_1 = Restaurant("Taj Hotel","Fast Food")
Restaurant_2 = Restaurant("Pinki Dabha","Deshi Food")
Restaurant_3 = Restaurant("SambharSa","South Indian")

Restaurant_1.describe_restaurant()
Restaurant_2.describe_restaurant()
Restaurant_3.describe_restaurant()
