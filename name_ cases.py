"""
man_name = "Eric"
man_name_1 = "petric"
man_name_2 = " Oleg"
man_name_3 = " Vas "
man_name_4 = "Nik  "
print("Hello" + " " + man_name + " " + ", would you like to learn some Python today?")
print(man_name)
print(man_name.title())
print(man_name_1.title())
print(man_name.upper())
print(man_name.lower())
print(man_name_2)
print(man_name_2.lstrip())
print(man_name_3)
print(man_name_3.lstrip())
print(man_name_3.rstrip())
print(man_name_3.strip())
print(man_name_4)
print(man_name_4.rstrip())
# Paul. lo-lo-lo
import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[2].title())
bicycles[0]='ukr'
print(bicycles)
bicycles.append('bak')
print(bicycles)
bicycles.insert(-1, "rOOGA")
print(bicycles)
bicycles.append('nothing')
print(bicycles)
print(bicycles[4].title())
print(bicycles.remove('nothing'))
print(bicycles)
guests=['oli', 'boli', 'dol']
print("Hello " + guests[1].title() + " her")
print(guests.pop(2).title())
print(guests)
guests.append('tolli')
print(guests)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_sorted = sorted(cars, reverse=True)
print("\n", cars_sorted)
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)
print(sorted(cars, reverse=True))
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(magician)
print(*[magician for magician in magicians], sep="\n")
print(*magicians, sep="\n")
print(*dir(magicians), sep="\n")
print(magicians.__doc__)
print(magicians.__repr__)
print(magicians.__str__)

print(magicians.__repr__())
print(magicians.__str__())
print(dir(magicians.__reversed__().__class__))
pizzas=['chili', 'seeer', 'Paper']
for pizza in pizzas:
   print("\n I like " + pizza)
   print(*pizzas)
print("enough")
for value in range(1,11):
	print(value)
case = [value for value in range(1,21)]
print(case)
case = [value for value in range(5,1000001)]
print(min(case))
print(max(case))
print(sum(case))
numbers=[value for value in range(1,20,2)]
print(numbers)
numbers1=[value for value in range(3,30,3)]
print(numbers1)
numbers2=[value**3 for value in range(1,10)]
print(numbers2)
numbers3=[value for value in range(1,10)]
print(numbers3)
mail=['qa', 'qc', 'jun', 'mid']
print(mail)
new_mail = mail[:]
print(new_mail)
mails_type = 'sin'
mails_type2 = 'lead'
mails_type3 = 'qa'
if mails_type in mail:
	print("Zhest")
if mails_type2 not in mail:
	print("norm")
if mails_type3 in mail:
	print("otl")
'sin' in mail
'lead' in mail
'qa' in mail
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Ohh, Sorry, you are too young to vote.")
    print("Ahh, Please register to vote as soon as you turn 18!")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
print("___________________________________")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
   if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
else:
    print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
print("___________________________________")

guys = ['rab', 'bos','admin', 'VAS', 'alex']
for guy in guys:
	if guy == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:    
	    print("Hello " + guy + ", thank you for logging in again")
print("_" * 50)

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Shalom")
print("We need to find some users!")
print("___________________________________")
guys = ['rab', 'Bos','admin', 'VAS', 'alex']
guys2 = ['rab', 'bos', 'sem', 'admin', 'vas']	
for guy in guys:
	if guy in guys2:
		print("My guys " + guy)
	elif guy not in guys2:
		print("Your guys " + guy)
	else:
		print("Bye")
print("-" * 50)	
for guy in guys2:
	if guy not in guys:
		print("Your guys " + guy)
print("-" * 50)	
for guy in guys2:
	if guy.title() in guys:
		print("This " + guy)
print("-" * 50)	
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
}
print("Sarah's favorite language is " 
	+ favorite_languages['sarah'].title() 
	+ ".")
favorite_languages['edward']
user_0 = {
   'username': 'efermi',
   'first': 'enrico',
   'last': 'fermi',
   }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
user_0['bd'] = 'eigh'   
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("-" * 50)	
for user_name in user_0.keys():
	print("Name1 " + user_name)
print("-" * 50)
for user_name in user_0.values():
	print("Name2 " + user_name)
list = ['jek', 'fermi', 'bic', 'efermi']
list2 = ['jek', 'fermi', 'bic', 'efermi']
for name in user_0.values():
	if name in list:
		print(" opa " + name)
print("-" * 50)
aliens = []
for alien_number in range(4):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    for alien in aliens[:2]:
        print(alien)
print("...")
people_firs1 = {'fname' : 'vas', 'lname' : 'boo', 'city' : 'kyi'}
for fdate, secdate in people_firs1.items():
	print("Opaa " + fdate.title() + " " + secdate.title())
people_sec2 = {'fname' : 'mak', 'lname' : 'err', 'lname' : 'berl'}
people_third3 = {'fname' : 'ole', 'lname' : 'fdd', 'lname' : 'oslo'}
people_all = {'people_firs1': {
	'fname' : 'vas',
	'lname' : 'boo', 
	'city' : 'kyi'
	},
	'people_sec2': {
	'fname' : 'mak', 
	'lname' : 'err', 
	'lname' : 'berl'
	},
	'people_third3': {
	'fname' : 'ole', 
	'lname' : 'fdd', 
	'lname' : 'oslo'
	},
	}
for fdate5, secdate5 in people_all.items():
	print(fdate5)
	print(secdate5)
	
	new_secdate = secdate5['lname']
	print("Opaa " + fdate5 + " " + new_secdate.title())
mess = input("Go Broooo:")
print(mess)
age = input("How old are you? ")
age = int(age)
age >= 18
cars = input("Which car: ")
print("Let me see if I can find you a " + cars)
table = input("How many people " )
number_table = int(table)
if number_table <= 8:
	print("Ooook")
else:
	print("Byeeeeee")
atable = input("Dataaa " )
enumber_table = int(atable)
if enumber_table % 10 == 0:
	print("great")
else:
	print("Vasya")
while True:
    pizza = input("Enter pizza: ")
    if pizza != 'quit':
	    print("Oook " + pizza)
    else:
	    print("Buyee")
	    break;
"""
"""
while True:
	age = input("Inpuut age: ")
	whole_age = int(age)
	if whole_age <= 3:
	    print("Free: " + str(whole_age))
	elif whole_age >= 4 and whole_age <= 10:
	    print("It costs: " + str(whole_age))
	elif 11 <= whole_age <= 15:
	    print("It should cost: " + str(whole_age))
	elif whole_age >= 16:
	    print("It costs: " + str(whole_age))
	    print(f"It costs: {whole_age}")
	    print("It costs: {0}".format(whole_age))
	    print("It costs: {whole_age}".format(whole_age=whole_age))
	else:
	    print("You are pensioner: " + str(whole_age))
	    
"""
"""
sandwich = ['meat','pasta','salo','tomat', 'pasta', 'bread']  
final_sandw = []  
for ingrid in sandwich:
	print("I made with: " + ingrid)
while sandwich:
	if 'pasta' in sandwich:
		sandwich.remove('pasta')
	new_ing = sandwich.pop()
	final_sandw.append(new_ing)
for all_ingrid in final_sandw:
	print("New made with: " + all_ingrid)
"""
"""
def favorite_book(title):
	print("One of my favorite books is Alice in Wonderland and " + title.title())
favorite_book('shalom')
	
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
 
"""
"""
def city_country(city, country):
	place = city + " " + country
	return print(place.title())

city_country('kiev', 'ukraine')
city_country('vepr', 'win')
city_country('gadiach', 'boss')
"""
"""
def make_album(singer,album,way = ''):
    full_alb = {'name' : singer, 'aname' : album}
    if way:
    	full_alb['way'] = way
    return full_alb

print(make_album('nat' , 'her'))
print(make_album('got' , 'er', 'dod'))
print(make_album('bit' , 'rr'))
"""
"""
def make_album(singer,album,way = ''):
    full_alb = {'name' : singer, 'alname' : album}
    if way:
    	full_alb['way'] = way
    return full_alb

while True:
	enter_name = input("Enter name: ")
	enter_album = input("Enter album: ")
	if enter_name == 'q':
	    break
	if enter_album == 'q':
		break
	new_alb = make_album(enter_name, enter_album)
	print(new_alb)
"""
"""
list1 = ['sad','bad','ret','git']
new_list = []
def give_list(list_name):
	for klik_name in list_name:
		print("My list_name is: " + klik_name)

give_list(list1)

#def make_great(give_list[:],new_give_list):

def make_great(list1, new_list):
	while list1:
		temp_name = list1.pop()
		full_temp = 'Great' + temp_name
		new_list.append(full_temp)
		for n_list in new_list:
		    print(n_list)
		    
make_great(list1[:], new_list)
"""
"""
def sandwich(*components):
	for component in components:
	    print("opoooo " + component + " yea")		

sandwich('red','dark','blue','green')
"""
"""
def my_profile(fname,lname,age, **user_info):
	profile = {}
	profile['fname']=fname
	profile['lname']=fname
	profile['age']=fname
	for key, value in user_info.items():
		profile[key] = value
	return profile

print(my_profile('vas','alibaba','old', positions='sesurity', state = 'private'))
"""


def my_profile(fname, lname, age, **user_info):
	profile = {}
	profile['fname'] = fname
	profile['lname'] = fname
	profile['age'] = fname
	for key, value in user_info.items():
		profile[key] = value
	return profile


print(my_profile('vas', 'alibaba', 'old', positions='sesurity', state='private'))
