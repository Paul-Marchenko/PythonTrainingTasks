import  json

def shalom_man():
    file_name = 'username.json'

    try:
        with open(file_name) as m3_file:
            username = json.load(m3_file)
    except FileNotFoundError:
        username = input("your name: ")
        with open(file_name, 'w') as m4_f:
            json.dump(username, m4_f)
            print("u name " + username)
    else:
        print("shallllom " + username)


shalom_man()