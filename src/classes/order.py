# Class for ordering drinks/ noting down what people want in a 'round'
# OOP day one
# 14/09/2020

from src.output.tables import generate_table , print_table
from src.persistence.data_persistence import preferences_dict


class Order:
    def __init__(self):
        self.order = {}

    def add_to_order(self, name, drink=None):
        # Add a person from people_dict and their drink order from drinks_dict
        # Update preferences
        if drink:
            self.order[name] = drink
        elif name in preferences_dict:
            self.order[name]= preferences_dict[name]
        else:
            print(f'Could not take order.\nYou did not input a drink and a preference is not saved for {name}.')


    def print_order(self):
        print_table(generate_table('Order',self.order))


# drink_round = Order()
# drink_round.print_order()
# drink_round.add_to_order("Kathryn","English Breakfast")
# drink_round.add_to_order("Katy")
# drink_round.print_order()
# print(drink_round.order)


#TODO: Add in functionality to store previous orders?
