import connect_db as connect


def show_film(cnx):
    request = cnx.cursor()
    request.execute('select title,length from film;')
    result = request.fetchall()
    for table in result:
        print('->',table[0],'-',table[1],'min')


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    request = cnx.cursor()
    request.execute('select title,length from film;')
    result = request.fetchall()
    for table in result:
        print('->',table[0],'-',table[1],'min')
