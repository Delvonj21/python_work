class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Welcome to {self.restaurant_name}, we got the best {self.cuisine_type} in the Chi!"
        )

    def open_restaurant(self):
        print("We are open!")


restaurant = Restaurant("Home Run Inn", "pizza")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

harold = Restaurant("Harold's", "chicken")
big_boys = Restaurant("Big Boys", "garlic fries")
harold.describe_restaurant()
big_boys.describe_restaurant()
