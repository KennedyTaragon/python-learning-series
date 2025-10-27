username = input("Enter your Desired Username: ")

def hint_username(username):
    if len(username) < 5:
        print("Invalid username. Must be at least 5 characters long")
    else:
        print("Valid username")

hint_username(username)