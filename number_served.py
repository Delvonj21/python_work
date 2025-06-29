class Restaurant:
    # A class representing a restaurant

    def __init__(self, name, cuisine_type):
        # Initialize the restaurant
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        # Display a description of the restaurant
        msg = f"{self.name} serves the best {self.cuisine_type} in the city!"
        print(f"\n{msg}")

    def open_restaurant(self):
        # Display a message that the restaurant is open
        msg = f"{self.name} is open. Let's eat!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        # Let user set the number of people that have been served
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        # Let user to increment the number of customers served
        self.number_served += additional_served


restaurant = Restaurant("Home Run Inn", "pizza")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")
