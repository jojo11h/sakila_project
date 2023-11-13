import time
from connect_db import DatabaseManager as dataco
from actor_db import read_actor as ac, show_actors, show_actor, does_actor_exist, add_actor, delete_actor
from film_db import read_film as rf, show_film
from categorie_db import read_categorie as rc, show_category

cnx = dataco('root', 'sakila')

while True:
    print("_" * 50)
    print()
    print("Que veux tu faire :")
    print("-> 1. Voir le contenu (Film, Acteur, Catégorie)")
    print("-> 2. Modifier le contenu (Ajout, Modification, Suppression)")
    print('-> "q pour quitter ')
    user_choice = input("=> ")

    if user_choice == "q":
        break

    if user_choice not in ["1", "2"]:
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
                                print("-> 2. Voir un acteur (recherche par nom)")
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
                                            print("le nom de l'acteur : ")
                                            show_actor(cnx,
                                                       input("=>"))
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
                            case "3":
                                print("_" * 50)
                                print()
                                print("Que veux tu Faire")
                                print("-> 1. Voir toutes les categories")
                                print("-> 2. Recherche film par categorie")
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
                                            show_category(rc(cnx))
                                            time.sleep(1.5)
                                        case "2":

                                            time.sleep(1.5)
                                            pass
                                        case "3":
                                            time.sleep(1.5)
                                            pass
                                        case _:
                                            print("essais")
            case '2':
                while True:
                    print("_" * 50)
                    print()
                    print("Que veux tu modifier")
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
                                print("Que veux tu faire")
                                print("-> 1. Ajouter un Acteur")
                                print("-> 2. Modifier les données sur un acteur")
                                print("-> 3. Supprimer un acteur")
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
                                            print(
                                                "Quel acteur souhaite-tu ajouter ?")
                                            print("-> Rentre son prenom")
                                            first_name_select = input("=> ")
                                            print("-> Rentre son nom")
                                            last_name_select = input("=> ")
                                            add_actor(
                                                cnx, first_name_select, last_name_select)
                                        case "2":
                                            print("_" * 50)
                                            print()
                                            print(
                                                "Quel acteur souhaite-tu modifier ?")
                                            print("-> Rentre son nom")
                                            last_name_select = input("=> ")
                                            does_actor_exist(
                                                cnx, last_name_select)
                                        case '3':
                                            print("_" * 50)
                                            print()
                                            print(
                                                "Quel acteur souhaite-tu supprimer ?")
                                            delete_actor(cnx, input("=> "))

# if __name__ == '__main__':

#     request = cnx.cursor()
#     request.execute('select * from actor;')
#     result = request.fetchall()
#     for row in result:
#         print(row[0] -1)
