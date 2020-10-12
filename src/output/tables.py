# Table creation helper variables
SPACER = ' '

# Table output helper functions

def get_table_width(header,data):
    #TODO: doesn't deal with data = None
    max_length = len(header)
    for item in data.values():
        if len(item) > max_length:
            max_length = len(item)
    return max_length

def get_key_width(data):
    # print(data)
    max_width=0
    for key in data.keys():
        if len(str(key)) > max_width:
            max_width = len(str(key))
    return max_width

# Add a horizontal break line +====+
def add_breakline(width,key_width, table_list):
    # Handle key_width = 0 when table empty
    if key_width == 0:
        key_width = 1
    table_list.append(f"+{(key_width +3)*'='}+{(width)*'='}+")
    return table_list

# Prints a header for the table
def add_header(header,width,key_width, table_list,header2 = 'KEY'):
    table_list = add_breakline(width,key_width,table_list)
    table_list.append(f'|{header2}{SPACER * (key_width - len(header2)+3)}|{header.upper()}{SPACER * (width - len(header))}|')
    table_list = add_breakline(width,key_width,table_list)
    return table_list

# Generates the table were each element in the list is a line in the table

def generate_table(header, data, header2=None):
    table_list = []
    width = get_table_width(header,data)
    key_width = get_key_width(data)
    if header2 == None:
        table_list = add_header(header,width,key_width,table_list)
    else:
        table_list = add_header(header,width,key_width,table_list,header2)
    for key,item in data.items():
        table_list.append(f'| {key} {SPACER * (key_width - len(str(key))+1)}|{item}{SPACER * (width - len(item))}|')
    table_list = add_breakline(width,key_width,table_list)
    return table_list

# Takes in list of table lines and prints them out
def print_table(table_list):
    for i in table_list:
        print(i)
    # print('\n'.join(table_list))

# Join two tables
def join_tables(table_list1 , table_list2):
    #TODO: change this to tuples?
    longest_table = table_list1
    shortest_table = table_list2
    if len(table_list1)<len(table_list2):
        longest_table = table_list2
        shortest_table = table_list1
    i=0
    while i in range(len(shortest_table)):
        longest_table[i] += shortest_table[i]
        i+=1
    return longest_table
