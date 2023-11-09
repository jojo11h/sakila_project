
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


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    actors = []
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for row in result:
        actors.append(ac.Actor(row[0],row[1],row[2],row[3]))
    for actor in actors:
        print(actor.first_name)
