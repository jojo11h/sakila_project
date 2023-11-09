import time
import connect_db as connect
from actor_db import read_actor as ac , show_actors
from film_db import read_film as rf, show_film

cnx = connect.call('root','sakila')

while True:
    print("_" * 50)
    print()
    print("Que veux tu faire :")
    print("-> 1. Voir le contenu (Film, Acteur)")
    print("-> 2. Modifier le contenu")
    print("-> 3. Supprimer du contenu")
    print('-> "q pour quitter ')
    user_choice = input("=> ")

    if user_choice == "q":
        break

    if user_choice not in ["1", "2", "3"]:
        print("Veuillez choisir une donnée valide !")

    else:
        match user_choice:
            case "1":
                while True:
                    print("_" * 50)
                    print()
                    print("Que veux tu voir")
                    print("-> 1. Les acteurs")
                    print("-> 2. Les Films")
                    print("-> 3. Les Catégories")
                    print('-> "q pour quitter ')
                    user_choice = input("=> ")

                    if user_choice == "q":
                        break

                    if user_choice not in ["1", "2", "3"]:
                        print("Veuillez choisir une donnée valide !")

                    else:
                        match user_choice:

                            case "1":
                                print("_" * 50)
                                print()
                                print("Que veux tu Faire")
                                print("-> 1. Voir tout les acteurs")
                                print("-> 2. *")
                                print("-> 3. *")
                                print('-> "q pour quitter ')
                                user_choice = input("=> ")

                                if user_choice == "q":
                                    break

                                if user_choice not in ["1", "2", "3"]:
                                    print("Veuillez choisir une donnée valide !")

                                else:
                                    match user_choice:
                                        case "1":
                                            show_actors(ac(cnx))
                                            time.sleep(1.5)
                                        case "2":

                                            time.sleep(1.5)
                                            pass
                                        case "3":
                                            time.sleep(1.5)
                                            pass
                                        case _:
                                            print("essais")
                            case "2":
                                print("_" * 50)
                                print()
                                print("Que veux tu Faire")
                                print("-> 1. Voir tout les films")
                                print("-> 2. *")
                                print("-> 3. *")
                                print('-> "q pour quitter ')
                                user_choice = input("=> ")

                                if user_choice == "q":
                                    break

                                if user_choice not in ["1", "2", "3"]:
                                    print("Veuillez choisir une donnée valide !")

                                else:
                                    match user_choice:
                                        case "1":
                                            show_film(rf(cnx))
                                            time.sleep(1.5)
                                        case "2":

                                            time.sleep(1.5)
                                            pass
                                        case "3":
                                            time.sleep(1.5)
                                            pass
                                        case _:
                                            print("essais")


# if __name__ == '__main__':
#     request = cnx.cursor()
#     request.execute('select * from actor;')
#     result = request.fetchall()
#     for row in result:
#         print(row[0] -1)
