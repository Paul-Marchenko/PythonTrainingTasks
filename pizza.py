#from making_pizzas import sandwich

print("_" *50)
def make_pizza(size, *toppings):
       """Выводит описание пиццы."""
       print("\nMaking a " + str(size) +
             "-inch pizza with the following toppings:")
       for topping in toppings:
           print("- " + topping)

def my_profile(fname,lname,age, **user_info):
	profile = {}
	profile['fname']=fname
	profile['lname']=fname
	profile['age']=fname
	for key, value in user_info.items():
		profile[key] = value
	return profile

#print(my_profile('vas','alibaba','old', positions='sesurity', state = 'private'))

#sandwich('red','dark','blue','green')
print("_" *50)
