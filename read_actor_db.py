
import actor as ac

def read_actor(cnx):
    actors = []
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for row in result:
        result[row[0] -1] = ac.Actor(row[0],row[1],row[2],row[3])
        actors.append(result[row[0]-1])
