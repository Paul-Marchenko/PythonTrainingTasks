
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print("Our rstaurant is: " + self.restaurant_name.title() +
		      " with " + self.cuisine_type + " cuisine.")
	def open_restaurant(self):
		print("Restaurant is opened")
		
	def set_number_served(self, quant):
		self.number_served = quant
	def increment_number_served(self, quest):
		self.number_served += quest
		
		

new_rest = Restaurant('Terra', 'gergian')
new_rest.describe_restaurant()
new_rest.open_restaurant()
first_r = Restaurant('Gera', 'turgian')
first_r.describe_restaurant()
second_r = Restaurant('Hara', 'belgian')
second_r.describe_restaurant()
restik = Restaurant('Bura', 'norweyn')
temp1 = restik.number_served
print(temp1)
restik.number_served = 3
temp2 = str(restik.number_served)
print(temp2)
print("_" *50)

restik.set_number_served(8)
print(restik.number_served)
print("_" *50)
restik.increment_number_served(1)
print(restik.number_served)
print("_" *50)