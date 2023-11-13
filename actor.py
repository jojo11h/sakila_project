import connect_db as connect


class Actor():
    def __init__(self, id, first_name, last_name) -> None:
        self._id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"-> {self.id} - {self.last_name} {(self.first_name).capitalize()}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @id.deleter
    def id(self):
        del self._id

    def update_actor(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def insert_actor(self):
        self.id
        self.first_name
        self.last_name


if __name__ == '__main__':
    cnx = connect.call('root', 'sakila')
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for table in result:
        print(table)

    # actor_to_update = Actor(id=1, first_name='NewFirstName', last_name='NewLastName', last_update=None)
    # actor_to_update.update_actor('UpdatedFirstName', 'UpdatedLastName')
