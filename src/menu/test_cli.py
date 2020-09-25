import unittest
from unittest.mock import Mock, patch

from menu.cli import print_menu 
from menu.cli import (GET_PEOPLE, 
GET_DRINKS,
GET_PREFERENCES, 
GET_ORDER, 
ADD_PERSON, 
ADD_DRINK,
ADD_PREFERENCE,
MAKE_ORDER, 
EXIT)
from menu.cli import add_person, add_drink

#NOTE: dpcs for unittest.mock 
# https://docs.python.org/3/library/unittest.mock.html

class Test_cli(unittest.TestCase):
    @patch("builtins.input")
    def test_input_of_selection_in_print_menu(self, input_mock):
        # Arrange
        input_mock.return_value = '1'
        # Act
        returned_value = print_menu()
        # Assert
        self.assertEqual(input_mock.return_value,returned_value)
        self.assertEqual(input_mock.call_count,1)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_printing_in_print_menu(self, input_mock, print_mock):
        # Arrange
        input_mock.return_value = '1'
        # Act
        print_menu()
        # Assert
        print_mock.assert_called_once_with(f'''Please, select an option by entering a number:
    [{GET_PEOPLE}] Get all people
    [{GET_DRINKS}] Get all drinks
    [{GET_PREFERENCES}] Get all preferences
    [{GET_ORDER}] Get the order
    [{ADD_PERSON}] Add person
    [{ADD_DRINK}] Add drink
    [{ADD_PREFERENCE}] Save someone's favourite drink
    [{MAKE_ORDER}] Append to order
    [{EXIT}] Exit''')

    #===========================================================#
    def test_add_person(self):
        # Arrange
        data = {
        1: 'Emma', 
        2: 'Olivia', 
        3: 'Ava', 
        4: 'Isabella', 
        5: 'Sophia', 
        6: 'Charlotte', 
        7: 'Mia', 
        8: 'Kate', 
        9: 'Alan'
        }
        expected = {
        1: 'Emma', 
        2: 'Olivia', 
        3: 'Ava', 
        4: 'Isabella', 
        5: 'Sophia', 
        6: 'Charlotte', 
        7: 'Mia', 
        8: 'Kate', 
        9: 'Alan', 
        10: 'Tim'}

        # Act
        add_person('Tim',data)

        # Assert
        self.assertEqual(expected, data)

#==============================================================================#
    def test_add_drink(self):
        # Arrange
        data = {
        1: 'Tea', 
        2: 'Coffee', 
        3: 'Water', 
        4: 'Juice', 
        5: 'Beer', 
        6: 'Wine', 
        7: 'Gin', 
        8: 'Milk', 
        9: 'Vodka'
        }

        expected = {
        1: 'Tea', 
        2: 'Coffee', 
        3: 'Water', 
        4: 'Juice', 
        5: 'Beer', 
        6: 'Wine', 
        7: 'Gin', 
        8: 'Milk', 
        9: 'Vodka', 
        10: 'Rum'}
        # Act
        add_drink('Rum',data)

        # Assert
        self.assertEqual(expected, data)



if __name__ == "__main__":
    unittest.main()
