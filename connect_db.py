import mysql.connector as mysql

try:
    cnx = mysql.connect(host="127.0.0.1",
                         user='root',
                         password="",
                         database ='sakila')

except mysql.Error as e:
    print(e)

cursor = cnx.cursor()
