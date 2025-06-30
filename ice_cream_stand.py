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


class IceCreamStand(Restaurant):
    # Represent a Ice cream stand

    def __init__(self, name, cuisine_type="ice cream"):
        # Initialize attributes of Restaurant class
        # Then initialize attributes specific to an ice cream stand

        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        # Display available flavors

        print(f"\nWe have these flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cream = IceCreamStand("Cold Stone")
ice_cream.flavors = ["salty caramel", "chocolate", "vanilla"]

ice_cream.describe_restaurant()
ice_cream.show_flavors()
