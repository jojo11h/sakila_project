import film as f
from connect_db import DatabaseManager as dataco


def read_film(cnx):
    query = 'select * from film;'
    result = cnx.execute_query(query)
    films = [f.Film(row[0], row[1], row[2], row[3], row[4],
                    row[5], row[6], row[7], row[8], row[9], row[10], row[11]) for row in result]
    return films


def show_film(films):
    for film in films:
        print(film)


def add_film(cnx, title):
    all_film = read_film(cnx)
    new_film = f.Film(all_film[-1].film_id + 1, title)
    query = """INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
               VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"""
    data = (new_film.title, new_film.descr, new_film.release, new_film.lang_id, new_film.rent_dur,
            new_film.rent_rate, new_film.replc_cost, new_film.rating, new_film.spec_feat)

    cnx.execute_query(query, data, commit=True)


if __name__ == '__main__':
    cnx = dataco('root', 'sakila')
    add_film(cnx, 'test')
