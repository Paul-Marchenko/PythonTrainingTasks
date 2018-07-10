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

"""
#10-11 page 209

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
"""
#10-12 page209

def enter_favorite_number():
    my_favor_num = display_fav_number()
    if my_favor_num:
        print("your favor num is: " + my_favor_num)
    else:
        get_new_user_name()


def display_fav_number():
    file_place = 'my_numbers.json'

    try:
        with open(file_place) as file_1:
            my_favor_num = json.load(file_1)
    except FileNotFoundError:
        print("Something bed")
    except Exception:
        print("Something bed too")
    else:
        return my_favor_num



def get_new_user_name():
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
        print("your number is: " + favor_num)



enter_favorite_number()

"""
def enter_favorite_number():
    my_favor_num = display_fav_number()
    if my_favor_num:
        print("your favor num is: " + my_favor_num)
    else:
        get_new_user_name()


def display_fav_number():
    file_place = 'my_numbers.json'

    try:
        with open(file_place) as file_1:
            my_favor_num = json.load(file_1)
    except FileNotFoundError:
        print("Something bed")
    except Exception:
        print("Something bed too")
    else:
        return my_favor_num



def get_new_user_name():
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
        print("your number is: " + favor_num)



enter_favorite_number()

