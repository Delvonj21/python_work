class Restaurant:
    # A class representing a restaurant

    def __init__(self, name, cuisine_type):
        # Initialize the restaurant
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Display a description of the restaurant
        msg = f"{self.name} serves the best {self.cuisine_type} in the city!"
        print(f"\n{msg}")

    def open_restaurant(self):
        # Display a message that the restaurant is open
        msg = f"{self.name} is open. Let's eat!"
        print(f"\n{msg}")


restaurant = Restaurant("Home Run Inn", "pizza")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
