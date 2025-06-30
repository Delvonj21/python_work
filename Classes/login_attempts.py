class User:
    # simple user profile

    def __init__(self, first_name, last_name, username, email, location):
        # Initialize the user
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        # Display user information
        print(f"\n{self.first_name} {self.last_name}")
        print(f"    Username: {self.username}")
        print(f"    Email: {self.email}")
        print(f"    Location: {self.location}")

    def greet_user(self):
        # Display greeting to the user
        print(f"\nWelcome back, {self.username}")

    def increment_login_attempts(self):
        # Increment the value of login_attempts
        self.login_attempts += 1

    def reset_login_attempts(self):
        # Reset login_attempts
        self.login_attempts = 0


john = User("john", "doe", "johnnyD", "jDoe@example.com", "canada")
john.describe_user()
john.greet_user()

print("\nMaking 3 login attempts...")
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(f"    Login attempts: {john.login_attempts}")

print("Resetting login attempts...")
john.reset_login_attempts()
print(f"    Login attempts: {john.login_attempts}")
