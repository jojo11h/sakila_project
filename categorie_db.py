import categorie as cat
import connect_db as connect


def read_categorie(cnx):
    categories = []
    request = cnx.cursor()
    request.execute("SELECT * FROM category")
    result = request.fetchall()
    for row in result:
        categories.append(cat.Categorie(row[0], row[1]))
    return categories


def show_category(categories):
    for category in categories:
        print(category)


if __name__ == '__main__':
    categories = []
    cnx = connect.call('root', 'sakila')
    request = cnx.cursor()
    request.execute("SELECT * FROM category")
    result = request.fetchall()
    for row in result:
        categories.append(cat.Categorie(row[0], row[1]))
    for categorie in categories:
        print(categorie.name)
