
import actor as ac
import connect_db as connect


def read_actor(cnx):
    actors = []
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for row in result:
        result[row[0] - 1] = ac.Actor(row[0], row[1], row[2], row[3])
        actors.append(result[row[0]-1])
    return actors


def show_actors(actors):
    for actor in actors:
        print(actor)


def update_actor(cnx, first_name, last_name, id):
    request = cnx.cursor()
    request.execute(f'UPDATE actor SET first_name = {first_name}, last_name = {
                    last_name}, last_update = now() where actor_id = {id}')
    try:
        cnx.commit()
        print('Mise à jour effectué')
    except Exception as e:
        print(f"Erreur de mise à jours :{e}")


def add_actor(cnx, new_first_name, new_last_name):
    request = cnx.cursor()
    request.execute(f"insert into actor(first_name,last_name) values ('{
                    new_first_name}','{new_last_name}');")
    try:
        cnx.commit()
        print("Ajout effectué!")
    except Exception as e:
        print(f"Erreur lors de l'insertion de l'acteur : {e}")


def delete_actor(cnx, id):
    request = cnx.cursor()
    request.execute(f"delete from actor where actor_id = {id};")
    try:
        cnx.commit()
        print("Suppression effectué!")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'acteur : {e}")


if __name__ == '__main__':
    cnx = connect.call('root', 'sakila')
    request = cnx.cursor()
    request.execute(f"delete from actor where actor_id = 201;")
    cnx.commit()
