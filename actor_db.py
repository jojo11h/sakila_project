from connect_db import DatabaseManager as dataco
import actor as ac


def read_actor(cnx):
    query = 'SELECT * FROM actor;'
    result = cnx.execute_query(query)
    actors = [ac.Actor(row[0], row[1], row[2], row[3]) for row in result]
    return actors


def show_actors(actors):
    for actor in actors:
        print(actor)


# def is_valid_input(user_input):
#     try:
#         int(user_input)
#         return True
#     except ValueError:
#         return False


def does_actor_exist(cnx, last_name):
    query = f"SELECT * FROM actor WHERE last_name = '{last_name}';"
    result = cnx.execute_query(query)
    if len(result) == 1:
        return update_actor(cnx, result[0])
    elif len(result) > 1:
        for actor in result:
            print(actor)

    else:
        return False


def update_actor(cnx, actor_id):
    first_name = input("Entrez son prénom \n => ")
    last_name = input('Entrez son nom \n => ')
    query = f"UPDATE actor SET first_name = '{first_name}', last_name = '{
        last_name}', last_update = NOW() WHERE actor_id = {actor_id};"
    cnx.execute_query(query, commit=True)
    print("Mise à jour effectuée")


def add_actor(cnx, new_first_name, new_last_name):
    query = f"""insert into actor(first_name,last_name) values ('{
        new_first_name}','{new_last_name}');"""
    cnx.execute_query(query, commit=True)


def delete_actor(cnx, actor_id):
    # while True:
    # if is_valid_input(actor_id):
    query = f"delete from actor where actor_id = {actor_id};"
    cnx.execute_query(query, commit=True)
    # break
    # else:
    # actor_id = input('Donnez un ID valide : ')


if __name__ == '__main__':
    cnx = dataco('root', 'sakila')
    actors = read_actor(cnx)
    does_actor_exist(cnx, input("=> "))
