import connect_db as connect


def show_film(cnx):
    request = cnx.cursor()
    request.execute('select title,length from film;')
    result = request.fetchall()
    for table in result:
        print('->',table[0],'-',table[1],'min')

class Film():
    def __init__(self,film_id:int,title:str,descr:str,release:int,lang_id:str,vo:str,rent_dur:int,rent_rate:float,length:int,replc_cost:float,rating:str,spec_feat) -> None:
        self.film_id=film_id
        self.title=title
        self.descr=descr
        self.release=release
        self.lang_id=lang_id
        self.vo=vo
        self.rent_dur=rent_dur
        self.rent_rate=rent_rate
        self.length=length
        self.replc_cost=replc_cost
        self.rating=rating
        self.spec_feat=spec_feat

    def __str__(self) -> str:
        return f"{self.film_id} - {self.title} {self.length} mins"


if __name__ == '__main__':
    cnx = connect.call('root','sakila')
    request = cnx.cursor()
    request.execute('select title,length from film;')
    result = request.fetchall()
    for table in result:
        print('->',table[0],'-',table[1],'min')
