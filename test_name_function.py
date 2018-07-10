import unittest
import nose
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):

        formatted_name = get_formatted_name('janis', 'joplin', 'vasilisa')
        try:
            if True:
                self.assertEqual(formatted_name, 'Janis Vasilisa Joplin')

        except AssertionError:

            print("Test 'test_first_last_name' is FAILED")
            # #print('\'', formatted_name, '\'')
            print("'{}'".format(formatted_name) + " != " 'Janis Vasilisa Joplin')
        else:
            print("Test 'test_first_last_name' is passed")


#unittest.main()