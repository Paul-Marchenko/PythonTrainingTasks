import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as m5:
            username = json.load(m5)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username


def get_new_username():
    username = input("Nu ih ")
    filename = 'username.json'
    with open(filename, 'w')as m5:
        json.dump(username, m5)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Hi " + username)
    else:
        username = get_new_username()
        print("Hello " + username)


greet_user()





