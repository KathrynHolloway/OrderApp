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

    def save_person(self, person_id, person_name):
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                data = [person_id, person_name]
                sql = 'INSERT INTO people (person_id, person_name) VALUES (%s, %s)'
                cursor.execute(sql, data)
                connection.commit()
        finally:
            connection.close()

    # Load drinks
    def load_people(self):
        data = {}
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * from people'
                cursor.execute(sql)
                while True:
                    people_data = cursor.fetchone()
                    if not people_data:
                        break
                    data[people_data[0]] = people_data[1]
                connection.commit()
        finally:
            connection.close()
        return data


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

    # Load drinks
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
people_dict = database.load_people()
