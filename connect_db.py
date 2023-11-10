import mysql.connector as mysql


def call(user,db):
    try:
        conn = mysql.connect(host ="127.0.0.1",
                            user = user,
                            password = "",
                            database = db)
    except mysql.Error as e:
            print(e)
    return conn

