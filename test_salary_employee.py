import unittest
import nose
from employee import Employee


class SalaryEmployeeTest(unittest.TestCase):
    def setUp(self):
        empl_charct = ('oleg', 'tarasov', 1700)
        self.current_empl = Employee(empl_charct)

    def test_give_default_raise(self):
        full_salary = self.current_empl.give_raise()
        #print(full_salary)
        self.assertEquals(full_salary, 6700)

    def test_give_custom_raise(self):
        full_salary = self.current_empl.give_raise(250)
        #print(full_salary)
        self.assertEquals(full_salary, 6950)

