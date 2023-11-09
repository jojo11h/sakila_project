import connect_db as cnx
result = cnx.cursor

def show_film():
    result.execute('select title,length from film;')
    for table in result:
        print('->',table[0],table[1]+'min')


if __name__ == '__main__':
    result.execute('select title,length from film;')
    for table in result:
        print('->',table[0],'-',str(table[1])+' min.')
