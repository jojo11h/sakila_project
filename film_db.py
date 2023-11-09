import film  as f
import connect_db as connect


def read_film(cnx):
    films = []
    request = cnx.cursor()
    request.execute('select * from actor;')
    result = request.fetchall()
    for row in result:
        result[row[0] -1] = f.Film(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
        films.append(result[row[0]-1])
    return films

def show_film(films):
    for film in films:
        print(film)


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    films = []
    request = cnx.cursor()
    request.execute('select * from film;')
    result = request.fetchall()
    for row in result:
        result[row[0] -1] = f.Film(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
        films.append(result[row[0]-1])
    # for film in films:
    #     print(films)
