# import pymysql
# from .env import mysql_pass
#NOTE: SQL playground database https://www.w3schools.com/sql/trysql.asp?filename=trysql_asc

# def main():
#     connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "OrderApp" )
#     cursor = connection.cursor()
#     # cursor.execute("INSERT INTO drinks (drink_name) VALUES ('Rum')")
#     # connection.commit()
#     cursor.execute("SELECT drink_id, drink_name FROM drinks")

#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
    
#     cursor.close()
#     connection.close()

# if __name__ == "__main__":
#     main()



import pymysql

class MySQLDB:
    def __init__(self, host='localhost', db_name="OrderApp", port=33066, user="root", password="password"):
        self.__host = host
        self.__db_name = db_name
        self.__port = port
        self.__user = user
        self.__password = password

    def __make_connection(self):
        return pymysql.connect(host=self.__host,
                               user=self.__user,
                               password=self.__password,
                               db=self.__db_name,
                               port=self.__port)

    # def load_people(self):
    #     data = []
    #     connection = self.__make_connection()
    #     try:
    #         with connection.cursor() as cursor:
    #             sql = f'SELECT * FROM {PERSON_TABLE}'
    #             cursor.execute(sql)
    #             while True:
    #                 person_data = cursor.fetchone()
    #                 if not person_data:
    #                     break
    #                 data.append(Person(
    #                             person_data[PERSON_ID_INDEX],
    #                             person_data[PERSON_FIRST_NAME_INDEX],
    #                             person_data[PERSON_LAST_NAME_INDEX],
    #                             person_data[PERSON_DRINK_NAME_INDEX],
    #                             ))
    #         connection.commit()
    #     finally:
    #         connection.close()
    #     return data

    # def insert_person(self, person):
    #     connection = self.__make_connection()
    #     try:
    #         with connection.cursor() as cursor:
    #             data = [str(person.id), person.first_name,
    #                     person.last_name, person.age]
    #             sql = f'INSERT INTO {PERSON_TABLE} ({PERSON_ID_COLUMN}, {PERSON_FIRST_NAME_COLUMN}, \
    #                 {PERSON_LAST_NAME_COLUMN}, {PERSON_AGE_COLUMN}) VALUES (%s, %s, %s, %s)'
    #             cursor.execute(sql, data)
    #             connection.commit()
    #     finally:
    #         connection.close()


    def save_drink(self, drink_id, drink_name):
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                data = [drink_id, drink_name]
                sql = 'INSERT INTO drinks (drink_id, drink_name) VALUES (%s, %s)'
                cursor.execute(sql, data)
                connection.commit()
        finally:
            connection.close()

    # Load drinks - match input/output to save to file drinks function
    def load_drinks(self):
        data = {}
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * from drinks'
                cursor.execute(sql)
                while True:
                    drink_data = cursor.fetchone()
                    if not drink_data:
                        break
                    data[drink_data[0]] = drink_data[1]
                connection.commit()
        finally:
            connection.close()
        return data


database = MySQLDB()

drinks_dict = database.load_drinks()
print(database.load_drinks())