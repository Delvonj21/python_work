class User:
    # simple user profile

    def __init__(self, first_name, last_name, username, email, location):
        # Initialize the user
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        # Display user information
        print(f"\n{self.first_name} {self.last_name}")
        print(f"    Username: {self.username}")
        print(f"    Email: {self.email}")
        print(f"    Location: {self.location}")

    def greet_user(self):
        # Display greeting to the user
        print(f"\nWelcome back, {self.username}")


john = User("john", "doe", "johnnyD", "jDoe@example.com", "canada")
john.describe_user()
john.greet_user()

jane = User("jane", "doe", "janeD", "jaDoe@example.com", "canada")
jane.describe_user()
jane.greet_user()
