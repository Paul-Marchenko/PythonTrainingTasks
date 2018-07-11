
class Employee:
    def __init__(self, full_info):
        self.name = full_info[0]
        self.surname = full_info[1]
        self.salary = full_info[2]
        self.full_info = full_info
        # self.full_info = name, surname, self.salary)

        print("New employee is " + self.full_info[0].title()
              + " " + self.full_info[1].title()
              + " with salary " + str(self.full_info[2]))
        # print("New employee is " + self.name.title() + " " + self.surname.title() + " with salary " + str(self.salary))

    def give_raise(self, range=0, permanent_salary=5000):
        self.salary = int(self.salary + permanent_salary + range)
        print("My new salary is: " + str(self.salary) + " and it was raised to " + str(range))
        return self.salary


info = ('vasya', 'alibaba', 1700)
new_empl = Employee(info)
new_empl.give_raise(0)
new_empl.give_raise(250)



"""
class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        print("New employee is " + self.name.title() + " " + self.surname.title() + " with salary " + str(self.salary))

    def give_raise(self, range, permanent_salary=5000):
        self.salary = str(self.salary + permanent_salary + range)
        print("My new salary is: " + str(self.salary) + " and it was raised to " + str(range))


new_empl = Employee('vasya', 'alibaba', 2000)
new_empl.give_raise(1500)
"""