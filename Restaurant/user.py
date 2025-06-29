class User:
    def __init__(self, first_name, last_name, age, hobbies):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbies = hobbies

    def describe_user(self):
        print(
            f"My name is {self.first_name} {self.last_name},I'm {self.age} years old and I like to {self.hobbies} in my free time."
        )

    def greet_user(self):
        print(f"Hey! {self.first_name}, it's nice to meet you!")


john_doe = User("John", "Doe", 99, "Bass fishing")
jane_doe = User("Jane", "Doe", 98, "annoying John Doe")

john_doe.describe_user()
john_doe.greet_user()

jane_doe.describe_user()
jane_doe.greet_user()
