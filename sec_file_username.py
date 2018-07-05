import json


def get_stored_username():


    filename = 'username.json'
    try:
        with open(filename) as m5:
            username = json.load(m5)
    except FileNotFoundError:
        return None
    else:
        return username

def shalom_man():
    username = get_stored_username()
    if username:
        print("Hi " + username)
    else:
        username = input("Nu ih " + username)
        filename = 'username.json'
        with open(filename)as m6:
            json.dump(username, 'w')
            print("Hello " + username)

shalom_man()
