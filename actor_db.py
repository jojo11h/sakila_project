
import actor as ac
import connect_db as connect


def read_actor(cnx):
    actors = []
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for row in result:
        result[row[0] -1] = ac.Actor(row[0],row[1],row[2],row[3])
        actors.append(result[row[0]-1])
    return actors


def show_actors(actors):
    for actor in actors:
        print(actor)

def update_actor(cnx,first_name,last_name,id):
    request = cnx.cursor()
    request.execute(f'UPDATE actor SET first_name = {first_name}, last_name = {last_name}, last_update = now() where actor_id = {id}')
    cnx.commit()


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    request = cnx.cursor()
    request.execute(f'UPDATE actor SET first_name = "PENELOPE", last_name = "GUINESS", last_update = now() where actor_id = 1')
    cnx.commit()

