import pymysql
# from .env import mysql_pass
#NOTE: SQL playground database https://www.w3schools.com/sql/trysql.asp?filename=trysql_asc

def main():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "OrderApp" )
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO drinks (drink_name) VALUES ('Rum')")
    # connection.commit()
    cursor.execute("SELECT drink_id, drink_name FROM drinks")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()