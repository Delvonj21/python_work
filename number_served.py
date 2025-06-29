class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"Welcome to {self.restaurant_name}, we got the best {self.cuisine_type} in the Chi! We currently have {self.number_served} customers. "
        )

    def open_restaurant(self):
        print("We are open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Home Run Inn", "pizza")
restaurant.describe_restaurant()

restaurant.number_served = 12
restaurant.describe_restaurant()

restaurant.set_number_served(24)
restaurant.describe_restaurant()

restaurant.increment_number_served(102)
restaurant.describe_restaurant()
