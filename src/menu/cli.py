import output.tables as t
import classes.order as order
import persistence.data_persistence as d
from persistence.data_persistence import people_dict, drinks_dict, preferences_dict, DRINKS_FILE, PEOPLE_FILE
# Input variables
GET_PEOPLE = '1'
GET_DRINKS = '2'
GET_PREFERENCES = '3'
GET_ORDER = '4'
ADD_PERSON = '5'
ADD_DRINK = '6'
ADD_PREFERENCE = '7'
MAKE_ORDER = '8'
EXIT = '9'

global new_order
new_order = order.Order()

# Menu creation functions
def print_menu():
    print(f'''Please, select an option by entering a number:
    [{GET_PEOPLE}] Get all people
    [{GET_DRINKS}] Get all drinks
    [{GET_PREFERENCES}] Get all preferences
    [{GET_ORDER}] Get the order
    [{ADD_PERSON}] Add person
    [{ADD_DRINK}] Add drink
    [{ADD_PREFERENCE}] Save someone's favourite drink
    [{MAKE_ORDER}] Append to order
    [{EXIT}] Exit''')
    user_input = str(input("Enter your selection: "))
    return user_input

# Prompts user to add an order to the order

def get_order_menu():
    add_order = True
    while add_order:
        choice = input('Do you want to add to the order? y/n:')
        if choice=='y':
            get_order(new_order)        
        elif choice == 'n':
            new_order.print_order()
            add_order = False
        else:
            # handle bad input
            #TODO
            continue
    # return new_order

def get_user_input():
    option = print_menu()
    if option == GET_PEOPLE :
        t.print_table(t.generate_table('people',people_dict))
        wait()
    elif option == GET_DRINKS:
        t.print_table(t.generate_table('drinks',drinks_dict))
        wait()
    elif option == GET_PREFERENCES:
        t.print_table(t.generate_table('preferences',preferences_dict))
        wait()
    elif option == GET_ORDER:
        new_order.print_order()
        wait()
    elif option == ADD_PERSON:
        name = get_name()
        add_person(name,people_dict)
        wait()
    elif option == ADD_DRINK:
        drink = get_drink()
        add_drink(drink,drinks_dict)
        wait()
    elif option == ADD_PREFERENCE:
        add_preference()
        wait()
    elif option == MAKE_ORDER:
        get_order_menu()
        wait()
    elif option == EXIT:
        if d.Data(DRINKS_FILE).save_data(drinks_dict) and d.Data(PEOPLE_FILE).save_data(people_dict):
            print('Saving data.....')
        print("CLOSING PROGRAM")
        pass
    #adds functionality for no input
    else:
        get_user_input()

def wait():
    input("Press ENTER to return to the menu:")
    get_user_input()

# Data alteration methods

def add_person(name, data):
    if name in data.values():
        # Tell user name already exists
        print(f'There is already a {name} in the list of people. Cannot add.')
        wait()
    elif name.isnumeric():
        # Tell user cannot accep numbers for names
        print(f'Numbers are not a valid name. \'{name}\' not added.')
        wait()
    else:
        new_key = 1
        if len(data.keys()) != 0:
            new_key = max(data.keys()) +1
        data[new_key] = name
        print(f'New person, {name}, added to list of people')

# Add drink
def add_drink(drink, data):
    if drink in data.values():
        # Tell user name already exists
        print(f'There is already a drink called \'{drink}\' in the list of drinks. Cannot add.')
    elif drink.isnumeric():
        # Tell user cannot accep numbers for drinks
        print(f'Numbers are not a valid drink name. \'{drink}\' not added.')
        wait()
    else:
        new_key = 1
        if len(data.keys()) != 0:
            new_key = max(data.keys()) +1
        data[new_key] = drink
        print(f'New drink, {drink}, added to list of drinks.')

# Save someone's preference
def add_preference():
    # TODO: Split this up into get_preference and add_preference
    people_table = t.generate_table('people',people_dict)
    drinks_table = t.generate_table('drinks',drinks_dict)
    table = t.join_tables(people_table,drinks_table)
    t.print_table(table)

    if len(people_table)<5:
        print('Sorry, it seems that there aren\'t any people saved to add a preference for.\nPlease add a person from the main menu.')
        get_user_input()        
    elif len(drinks_table)<5:
        print('Sorry, it seems that there aren\'t any drinks saved to choose as someone\'s preference.\nPlease add a drink from the main menu.')
        get_user_input()
    else:
        name_key = get_name_key()
        drink_key = get_drink_key()
        # Use keys to find corresponding values
        name = people_dict[name_key]
        drink = drinks_dict[drink_key]

        if name in preferences_dict:
            overwrite = input(f'{name} already has a favourite drink of {preferences_dict[name]}. \nDo you want to overwrite this to {drink}? y/n:')
            if overwrite.lower() == 'y':
                preferences_dict[name] = drink
            elif overwrite.lower() == 'n':
                print('Ok. Keeping existing data.')
            else:
                print('Sorry I didn\'t understand you. Data unchanged.')

        else:
            #add preference to dict
            preferences_dict[name] = drink
        
        t.print_table(t.generate_table('preferences', preferences_dict))

    


# Getter methods

# Get name
def get_name():
    name = str(input('Please enter the first name of the person you would like to add to the list: '))
    return name.title()

# Get drink
def get_drink():
    drink = str(input('Please enter the drink you would like to add to the list: '))
    return drink.title()

# Get name by key
def get_name_key():
    key = input('Please enter the corresponding key of the PERSON you would like to add a favourite drink for: ')
    while (not key.isnumeric() ) or (not int(key) in people_dict):
        if not key.isnumeric():
            key = input('''Your input must be a number.\nPlease enter the corresponding key of the PERSON you would like to add a favourite drink for: ''')
        else:
             key = input('Please enter a key that exists:')

    return int(key)


# Get drink by key
def get_drink_key():
    key = input('Please enter the corresponding key of the DRINK you would like to add as a favourite: ')
    while (not key.isnumeric() ) or (not int(key) in drinks_dict):
        if not key.isnumeric():
            key = input('''Your input must be a number.\nPlease enter the corresponding key of the DRINK you would like to save as a favourite: ''')
        else:
             key = input('Please enter a key that exists:')
    return int(key)

# Get someones order

def get_order(the_order):
    name = input('Please input the name of the person wanting to place an order:')
    drink = input(f'Enter the drink {name} wants or press ENTER if {name} wants their favourite:')
    if drink == '':
        drink = None
    the_order.add_to_order(name.title(),drink)
    
