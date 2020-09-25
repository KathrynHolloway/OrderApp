import classes.order as order
import unittest

# NOTE: Run with  py -m unittest classes.classes_tests from in src

class Test_Order(unittest.TestCase):
    def test_creating_empty_order(self):
        # Arrange
        expected_value = {}
        
        # Act
        new_order = order.Order()
        actual_value = new_order.order

        # Assert
        self.assertEqual(actual_value,expected_value)


if __name__ == "__main__":
    unittest.main()