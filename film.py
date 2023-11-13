import connect_db as connect


class Film():
    def __init__(self, film_id: int, title: str, descr: str = """Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum.""", release: int = 1990, lang_id: str = 2, vo: int = 5, rent_dur: int = 3, rent_rate: float = 03.10, length: int = 120, replc_cost: float = 015.20, rating: str = 'G', spec_feat="Deleted Scenes,Behind the Scenes") -> None:
        self.film_id = film_id
        self.title = title
        self.descr = descr
        self.release = release
        self.lang_id = lang_id
        self.vo = vo
        self.rent_dur = rent_dur
        self.rent_rate = rent_rate
        self.length = length
        self.replc_cost = replc_cost
        self.rating = rating
        self.spec_feat = spec_feat

    def __str__(self) -> str:
        return f"{self.film_id} - {self.title} ({self.length} mins)"


if __name__ == '__main__':
    cnx = connect.call('root', 'sakila')
    request = cnx.cursor()
    request.execute('select title,length from film;')
    result = request.fetchall()
    for table in result:
        print('->', table[0], '-', table[1], 'min')
