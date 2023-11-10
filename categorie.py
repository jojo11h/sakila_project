import connect_db as connect

class Categorie():
    def __init__(self,id,name) -> None:
        self.id = id
        self.name= name

    def __str__(self) -> str:
        return f"-> {self.name}"


if __name__ == "__main__":
    cnx = connect.call('root','sakila')
    request = cnx.cursor()
    request.execute("SELECT * FROM category")
    for table in request:
        print(table)
