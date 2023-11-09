import connect_db as cnx
result = cnx.cursor


def show_actor():
    result.execute('select first_name , last_name from actor;')
    for table in result:
        print('-',' '.join(table))



class Actor():
    def __init__(self,id,first_name,last_name) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name



