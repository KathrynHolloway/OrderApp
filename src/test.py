import unittest
from src.output.tables import get_key_width


# Class that inherits from TestCase in 
# the python standard library unittest
#NOTE: add failure case for adding person - try to input bad input then check the right thing happens
class Test_Methods(unittest.TestCase):
    # All tests must begin with test_
    
    def test_get_key_width(self):
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
        9: 'Alan', 
        10: 'Tim'}

        expected = 2
        # Act
        actual = get_key_width(data)

        # Assert
        self.assertEqual(expected, actual)

#==============================================================================#

if __name__ == '__main__':
    unittest.main()

