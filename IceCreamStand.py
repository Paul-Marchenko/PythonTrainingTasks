from restaurant import Restaurant
from user import User

class IceCreamStand(Restaurant):
	def __init__(self, flavors):
		self.flavors = flavors
		
	def write_list(self):
			
		print("Our list of: ", self.flavors)

green = IceCreamStand(['q','w','e'])
green.write_list()
		
class Admin(User):
	def __init__(self, privileges):
		self.privileges = privileges
	    
	def show_privileges(self):
		print("My previl: ", self.privileges)
		

list_of_priv = ['разрешено удалять пользователей','банить','добавлять']
rules = Admin(list_of_priv)
rules.show_privileges()
	
class Privileges():
    def __init__(self, privileges):
		self.privileges = privileges
    
		   
