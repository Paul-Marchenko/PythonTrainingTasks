import json

"""
def enter_favorite_number():
    file_place = 'my_numbers.json'

    try:
        favor_num = input("Your number: ")
        with open(file_place, 'w') as file_1:
            json.dump(favor_num, file_1)
    except FileNotFoundError:
        print("Something wrong")
    except Exception:
        print("Something wrong too")
    else:
        pass


def display_fav_number():
    file_place = 'my_numbers.json'

    try:
        with open(file_place) as file_1:
            my_fav_mun = json.load(file_1)
    except FileNotFoundError:
        print("Something bed")
    except Exception:
        print("Something bed too")
    else:
        print("your number is: " + my_fav_mun)


enter_favorite_number()
display_fav_number()
"""


def enter_favorite_number():
    file_place = 'my_numbers.json'

    try:
        favor_num = input("Your number: ")
        with open(file_place, 'w') as file_1:
            json.dump(favor_num, file_1)
    except FileNotFoundError:
        print("Something wrong")
    except Exception:
        print("Something wrong too")
    else:
        pass


def display_fav_number():
    file_place = 'my_numbers.json'

    try:
        with open(file_place) as file_1:
            my_fav_mun = json.load(file_1)
    except FileNotFoundError:
        print("Something bed")
    except Exception:
        print("Something bed too")
    else:
        print("your number is: " + my_fav_mun)


enter_favorite_number()
display_fav_number()
