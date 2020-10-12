# File manipulation
import csv

#am i supposed to create an instance of this class to hold say, people data and manipulte the 
# content of the class when say, adding people?
# or can i create an instance of the class and then assign its data content to a variable

class Data:

    def __init__(self, file_path):
        self.file_path = file_path
        # self.data = data

    # Parse file to dict
    def read_file(self):
        try:
            with open(self.file_path) as file:
                reader = csv.reader(file,quoting=csv.QUOTE_ALL)
                reader = list(reader)
                if len(reader) == 0:
                    cols = 0
                else:
                    cols = len(reader[0])
                
                content_dict = {}
                # Handle empty files
                if cols == 0:
                    print(f'{self.file_path} does not contain any data')
                # Handle 1D files like people and drinks
                elif cols == 1:
                    key = 1
                    for row in reader:
                        content_dict[key] = row[0]
                        key += 1
                # Handle 2D files like preferences
                elif cols == 2:
                    for row in reader:
                        content_dict[row[0]] = row[1]
                else:
                    print('This data has too many columns to proccess.')

                return content_dict

        except FileNotFoundError as e:
            print(f'Sorry there was a {e}.')

    # Save to file
    def save_data(self, data):
        with open(self.file_path,'w',newline='') as file:
            writer = csv.writer(file, quoting = csv.QUOTE_ALL)
            for value in data.values():
                writer.writerow([value])
        return True
    

# File data
# TODO: add this to main app file??
DRINKS_FILE = 'src/data/drinks.csv'
PEOPLE_FILE = 'src/data/people.csv'
PREFERENCES_FILE = 'src/data/preferences.csv'

# people_dict = Data(PEOPLE_FILE).read_file()
# drinks_dict = Data(DRINKS_FILE).read_file()
preferences_dict = Data(PREFERENCES_FILE).read_file()

# drinks_dict = Data()
# drinks_dict.read_file(PEOPLE_FILE)

# preferences_dict = Data()
# preferences_dict.read_file(PREFERENCES_FILE)

