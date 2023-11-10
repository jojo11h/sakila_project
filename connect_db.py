import mysql.connector as mysql


class DatabaseManager:
    def __init__(self, username, database):
        self.cnx = mysql.connect(host="127.0.0.1",
                                 user=username,
                                 password="",
                                 database=database)

    def __del__(self):
        if hasattr(self, 'cnx') and self.cnx.is_connected():
            self.cnx.close()

    def execute_query(self, query, commit=False):
        request = self.cnx.cursor()
        request.execute(query)
        if commit:
            try:
                self.cnx.commit()
            except Exception as e:
                print(f"Erreur lors de la validation de la transaction : {e}")
        return request.fetchall()
