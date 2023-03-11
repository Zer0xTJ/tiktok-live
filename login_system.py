# make a login system for multiple users
# create users in a list of dictionaries
# make a function for login that
# has 2 params (username, and pasword)

# create a functon for register new user

users = [
    {
        "username": "zer0xtj",
        "password": "123",
    },
    {
        "username": "amd4",
        "password": "1234",
    },
]

# should return true if user exists
# and fals if user not exists


def login(username, password):
    # loop on all users
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False


# recursion
# you have 3 tries
def login_input():
    for i in range(3):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if login(username, password):
            print("You logged in!")
            break
        else:
            print("Invalid credentials")


def reg():
    username = input("Enter username: ")
    password = input("Enter a password: ")
    # check if user exists
    for user in users:
        # user alreayd exists
        if user['username'] == username:
            print("User already exists!")
            return reg()

    # No users found for username
    users.append({
        "username": username,
        "password": password
    })
    print("register done!")


while True:
    print("Choose one: ")
    print("[r] - Register new account")
    print("[s] - Login to account")
    print("[q] - quit")
    choose = input("What do you want?: ")
    if choose == 'r' or choose == 'R':
        reg()
    elif choose.lower() == 's':
        login_input()
        break
    elif choose.lower() == 'q':
        break
    else:
        print('Invalid option/input!')
