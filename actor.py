import connect_db as connect

class Actor():
    def __init__(self,id,first_name,last_name,last_update) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    def __str__(self) -> str:
        return f"-> {self.id} - {self.last_name} {(self.first_name).capitalize()}"


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for table in result:
        print(table)
