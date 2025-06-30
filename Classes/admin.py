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


class Admin(User):
    # a user with admin privileges

    def __init__(self, first_name, last_name, username, email, location):
        # Initialize a admin

        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        # Display privileges this admin has

        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


john = Admin("john", "doe", "johnnyD", "jDoe@example.com", "canada")
john.describe_user()

john.privileges = ["can add post", "can delete post", "can ban user"]
john.show_privileges()
