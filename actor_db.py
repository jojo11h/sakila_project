from connect_db import DatabaseManager as dataco
import actor as ac


def read_actor(cnx):
    query = 'SELECT * FROM actor;'
    result = cnx.execute_query(query)
    actors = [ac.Actor(row[0], row[1], row[2]) for row in result]
    return actors


def show_actors(actors):
    for actor in actors:
        print(actor)


def does_actor_exist(cnx, last_name):
    query = "SELECT * FROM actor WHERE last_name = %s;"
    result = cnx.execute_query(query, (last_name,))

    if len(result) == 1:
        actor = ac.Actor(result[0][0], result[0][1], result[0][2])
        return update_actor(cnx, actor.id)
    elif len(result) > 1:
        id_result = []
        for actor in result:
            print('->', actor[0], actor[1], actor[2])
            id_result.append(str(actor[0]))
        print("Plusieurs résultats trouvés, entrez l'ID de l'acteur correspondant :")

        while True:
            user_id = input('=> ')
            if user_id not in id_result or not user_id.isdigit():
                print(id_result)
                print("Veuillez choisir une donnée valide !")
            else:
                update_actor(cnx, int(user_id))
                break
    else:
        print('Rien trouvé, entrez à nouveau un nom :')
        return does_actor_exist(cnx, input("=> "))


def show_actor(cnx, last_name):
    query = "SELECT * FROM actor WHERE last_name = %s;"
    result = cnx.execute_query(query, (last_name,))

    if len(result) == 1:
        actor = ac.Actor(result[0][0], result[0][1], result[0][2])
        return actor
    elif len(result) > 1:
        id_result = []
        print("Plusieurs résultats trouvés, entrez l'ID de l'acteur correspondant :")
        for actor in result:
            print('->', actor[0], actor[1], actor[2])
            id_result.append(str(actor[0]))

    else:
        print('Rien trouvé, entrez à nouveau un nom :')
        return show_actor(cnx, input("=> "))


def update_actor(cnx, actor_id):
    first_name = input("Entrez son prénom \n => ")
    last_name = input('Entrez son nom \n => ')
    query = "UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s;"
    data = (first_name, last_name, actor_id)
    cnx.execute_query(query, data, commit=True)
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
