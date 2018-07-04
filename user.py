class User:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.login_attempts = 0

    def increment_login_attempts(self, attempts):
        if attempts > 0:
            self.login_attempts = self.login_attempts + attempts

    def reset_login_attempts(self):
        if self.login_attempts > 0:
            self.login_attempts = 0


first_user = User('vasya', 'dvorn')
first_user.increment_login_attempts(3)
print(first_user.login_attempts)
first_user.increment_login_attempts(2)
first_user.increment_login_attempts(4)
print(first_user.login_attempts)

first_user.reset_login_attempts()
print(first_user.login_attempts)
